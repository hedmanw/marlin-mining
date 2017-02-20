#!/usr/bin/env python

from subprocess import Popen, PIPE
from shutil import copyfile, copytree, rmtree

import os, sys


class Merge:
    def __init__(self, base_commit, integration_commit, result, conflicts):
        self.base_commit = base_commit
        self.integration_commit = integration_commit
        self.result = result
        self.conflicts = conflicts

class Repo:
    def __init__(self, owner, repo_name):
        self.owner = owner
        self.repo_name = repo_name

    def clone_url(self):
        return "git@github.com:{}/{}".format(self.owner, self.repo_name)

    def __repr__(self):
        return self.owner + "/" + self.repo_name


class Commit:
    def __init__(self, repo, hash):
        self.repo = repo
        self.hash = hash

    def __repr__(self):
        return "{}#{}".format(self.repo, self.hash)


class Conflict:
    def __init__(self, filename, content, line_begin, line_end):
        self.filename = filename
        self.content = content
        self.line_begin = line_begin
        self.line_end = line_end


class Workspace:
    def __init__(self, prefix):
        self.prefix = prefix
        self.workspace_dir = prefix + "/merge_workspace"
        self.excerpts_dir = prefix + "/merge_excerpts"
        self.content_dir = prefix + "/whole_files"

    def main(self, base, integration, result):
        print "Cloning {}...".format(base.repo)
        self.clone(base.repo)

        print "Checking out {}".format(base.hash)
        self.checkout(base)

        merging_notice = "Merging {} with {}".format(base, integration)
        print merging_notice
        merge_output = self.merge(integration)

        print "Recorded merging status in README.md"
        conflict_files = self.format_conflicts(merge_output)

        makedir(self.excerpts_dir)
        commit_url = "https://github.com/{}/{}/commit/".format(base.repo.owner, base.repo.repo_name)
        with open(self.prefix + '/README.md', 'w') as f:
            def write(line):
                writeline(f, line)

            def link_to_commit(commit):
                return "{}{}".format(commit_url, commit)

            write("# {}".format(self.prefix))
            write("- Result commit: [{}]({})".format(result.hash, link_to_commit(result.hash)))
            write("- First parent (base): [{}]({})".format(base.hash, link_to_commit(base.hash)))
            write("- Second parent (remote): [{}]({})".format(integration.hash, link_to_commit(integration.hash)))

        #conflict_files = conflicts_sample.splitlines()
        print "Reading conflicts."
        conflicts = self.get_merge_excerpts(conflict_files)
        #conflicts = map(lambda x: Conflict(x, "", 0, 0), conflict_files)
        merge_instance = Merge(base, integration, result, conflicts)
        print "Storing excerpts of conflicts in merge_excerpts/"
        self.store_merge_excerpts(conflicts)
        print "Storing whole files in whole_files/"
        self.store_commit_contents(merge_instance)

        self.remove_workspace()


    def clone(self, repository):
        # github_url = repository.clone_url()
        # process, _, _ = self.git_process(["clone", github_url, self.workspace_dir])
        copytree("/tmp/Marlin", self.workspace_dir)

    def remove_workspace(self):
        rmtree(self.workspace_dir)

    def checkout(self, commit):
        process, stdout, stderr = self.git_process(["checkout", commit.hash], cwd=self.workspace_dir)

    def merge(self, commit):
        github_url = commit.repo.clone_url()
        merge_process, stdout, stderr = self.git_process(["pull", github_url, commit.hash], cwd=self.workspace_dir)
        return stdout

    def abort_merge(self):
        self.git_process(["merge", "--abort"], cwd=self.workspace_dir)

    def get_merge_excerpts(self, file_names):
        all_conflicts = []

        for file_name in file_names:
            file_conflicts = self.awk(file_name).split("<<<<<<<")[1:]
            for file_conflict in file_conflicts:
                all_conflicts.append(Conflict(file_name, file_conflict, 0, 0))

        print "  Storing snapshots of the merge (merge) in {}/".format(self.content_dir)
        self.copy_example_files(None, "merge", all_conflicts)
        self.abort_merge()

        return all_conflicts

    def store_merge_excerpts(self, conflicts):
        counter = 0
        for conflict in conflicts:
            source_file = conflict.filename
            qualified_source_name = source_file[source_file.index('/') + 1:]
            makedir(self.excerpts_dir)
            with open("{}/{}_{}".format(self.excerpts_dir, qualified_source_name, counter), 'w') as f:
                f.write("// EXCERPT FROM MERGE  {}\n\n".format(source_file))
                f.write("<<<<<<<" + conflict.content + "\n")
            counter += 1

    def store_commit_contents(self, merge):
        print "  Storing files in first parent (base) #{}".format(merge.base_commit.hash)
        self.copy_example_files(merge.base_commit, "base", merge.conflicts)
        print "  Storing files in second parent (remote) #{}".format(merge.integration_commit.hash)
        self.copy_example_files(merge.integration_commit, "remote", merge.conflicts)
        print "  Storing files in outcome (result) #{}".format(merge.result.hash)
        self.copy_example_files(merge.result, "result", merge.conflicts)

    def copy_example_files(self, commit, prefix, conflicts):
        makedir(self.content_dir)
        if commit:
            self.checkout(commit)
        for conflict in conflicts:
            source_file = conflict.filename
            qualified_source_name = source_file[source_file.index('/') + 1:]
            dir_source_file = self.workspace_dir + "/" + source_file
            dir_target_file = self.content_dir + "/" + prefix + "_" + qualified_source_name
            #print "Copying {} to {}.".format(dir_source_file, dir_target_file)
            copyfile(dir_source_file, dir_target_file)

    def awk(self, file_path):
        awk_process = Popen(["awk", "/<<<<<<< HEAD/,/>>>>>>>/", file_path], cwd=self.workspace_dir, stdout=PIPE, stderr=PIPE)
        stdout, stderr = awk_process.communicate()
        awk_process.wait()
        return stdout

    @staticmethod
    def git_process(args, cwd=None):
        args.insert(0, "git")
        process = Popen(args, cwd=cwd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        process.wait()
        return process, stdout, stderr

    @staticmethod
    def format_conflicts(merge_text):
        merge_lines = merge_text.splitlines()
        only_conflict_lines = lambda x: x.startswith("CONFLICT (content):")
        relevant_files = lambda x: not ("README.md" in x or ".gitignore" in x or "travis.yml" in x)
        only_filenames = lambda x: x[len("CONFLICT (content): Merge conflict in "):]
        return map(only_filenames, filter(relevant_files, filter(only_conflict_lines, merge_lines)))


def makedir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def writeline(file, line):
    file.write(line + "\n")


def read_commits_file(file_path):
    with open(file_path) as commits_file:
        return map(lambda _: _.strip().split(' '), commits_file.readlines())


if __name__ == '__main__':
    base_repo = Repo("MarlinFirmware", "Marlin")
    integration_repo = Repo("MarlinFirmware", "Marlin")

    commits = read_commits_file("merge-diffs/new-conflict-merges.txt")

    for i, conflict_merge in enumerate(commits[21:]):
        merge_commit = conflict_merge[0]
        first_parent = conflict_merge[1]
        second_parent = conflict_merge[2]
        print "{}/{} - {}".format(i+1, len(commits), merge_commit)

        base = Commit(base_repo, first_parent)
        result = Commit(base_repo, merge_commit)
        integration = Commit(integration_repo, second_parent)

        workspace = Workspace(result.hash[:7])
        workspace.main(base, integration, result)