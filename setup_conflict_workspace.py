#!/usr/bin/env python

from subprocess import Popen, PIPE
from shutil import copyfile

import glob
import os

temp_dir = "/tmp/"


class Repo:
    def __init__(self, owner, repo_name):
        self.owner = owner
        self.repo_name = repo_name

    def clone_url(self):
        return "git@github.com:{}/{}".format(self.owner, self.repo_name)

    def __repr__(self):
        return self.owner + "/" + self.repo_name


class Commit:
    def __init__(self, sha, first_parent_sha, second_parent_sha):
        self.sha = sha
        self.first_parent_sha = first_parent_sha
        self.second_parent_sha = second_parent_sha

    def __repr__(self):
        return "#{}".format(self.sha)


class Git:
    def __init__(self, repo):
        self.repo = repo

    def get_commit_parent(self, commit):
        process, stdout, stderr = self.git_process(["show", "--pretty=%P", commit])
        split_output = stdout.splitlines()
        return split_output[0]

    def checkout(self, commit):
        process, stdout, stderr = self.git_process(["checkout", commit])

    def clone(self):
        if not os.path.exists("{}{}".format(temp_dir, self.repo.repo_name)):
            print "Cloning {} into {}{}".format(self.repo, temp_dir, self.repo.repo_name)
            github_url = self.repo.clone_url()
            process, _, _ = self.git_process(["clone", github_url], cwd=temp_dir)
        else:
            print "Found repository {} in {}, will not clone again.".format(self.repo.repo_name, temp_dir)

    def get_log(self, commit):
        _, stdout, stderr = self.git_process(["show", commit])
        return stdout

    def get_conflicts(self, commit):
        log_output = self.get_log(commit).splitlines()
        conflicts_marker = "    Conflicts:"
        if conflicts_marker in log_output:
            conflicts_index = log_output.index(conflicts_marker)
            conflicting_files = map(lambda x: x.strip(), log_output[conflicts_index+1: -1])
            return conflicting_files
        return None

    def git_process(self, args, cwd=None):
        if not cwd:
            cwd = os.path.join(temp_dir, self.repo.repo_name)
        args.insert(0, "git")
        process = Popen(args, cwd=cwd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        process.wait()
        return process, stdout, stderr


class SubjectParser:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_commits(self):
        with open(self.file_name, 'r') as commits_file:
            return map(lambda _: _.strip(), commits_file.readlines())


class Workspace:
    def __init__(self, conflict_merge, git):
        self.conflict_merge = conflict_merge
        self.workspace_dir = conflict_merge[:7]
        self.git = git

    def populate(self):
        (valid, commit_ref) = self.get_parents()
        if valid:
            self.create()
            conflicts = self.calculate_conflict_files(commit_ref.sha)
            self.checkout_and_copy_conflicts(commit_ref.sha, "result", conflicts)
            self.checkout_and_copy_conflicts(commit_ref.first_parent_sha, "base", conflicts)
            self.checkout_and_copy_conflicts(commit_ref.second_parent_sha, "remote", conflicts)
            self.log_commit(commit_ref, conflicts)
        else:
            print "-- Commit {} was invalid.".format(self.conflict_merge)

    def log_commit(self, commit_ref, conflict_files):
        def link_to_commit(commit):
            return "https://github.com/{}/{}/commit/{}".format(git.repo.owner, git.repo.repo_name, commit)

        print "Writing log for {}".format(self.workspace_dir)
        with open(os.path.join(self.workspace_dir, "README.md"), 'w') as x:
            def write(line):
                writeline(x, line)
            write("# {}".format(self.workspace_dir))
            write("- Result commit: [{}]({})".format(commit_ref.sha, link_to_commit(commit_ref.sha)))
            write("- First parent (base): [{}]({})".format(commit_ref.first_parent_sha, link_to_commit(commit_ref.first_parent_sha)))
            write("- Second parent (remote): [{}]({})".format(commit_ref.second_parent_sha, link_to_commit(commit_ref.second_parent_sha)))
            write("")
            write("Conflicts:")
            for conflict_file in conflict_files:
                write("- {}".format(conflict_file))

    def checkout_and_copy_conflicts(self, sha, category, files_to_copy):
        self.git.checkout(sha)
        category_directory = os.path.join(self.workspace_dir, category)
        makedir(category_directory)

        for file_path in files_to_copy:
            copyfile(os.path.join(temp_dir, self.git.repo.repo_name, file_path), os.path.join(category_directory, os.path.basename(file_path)))

    def copy_all_source_code(self, sha, category):
        self.git.checkout(sha)

        cpp_files = glob.glob(os.path.join(temp_dir, self.git.repo.repo_name, "Marlin", "*.cpp"))
        header_files = glob.glob(os.path.join(temp_dir, self.git.repo.repo_name, "Marlin", "*.h"))
        self.checkout_and_copy_conflicts(sha, category, cpp_files + header_files)

    def create(self):
        makedir(self.workspace_dir)

    def get_parents(self):
        parent_shas = self.git.get_commit_parent(self.conflict_merge).strip().split(" ")
        return len(parent_shas) == 2, Commit(self.conflict_merge, parent_shas[0], parent_shas[1])

    def calculate_conflict_files(self, commit_sha):
        def only_marlin_files(file_path):
            return file_path.startswith("Marlin")
        # def  x: not ("README" in x or ".gitignore" in x or "travis.yml" in x)
        conflicting_files = self.git.get_conflicts(commit_sha)
        return filter(only_marlin_files, conflicting_files)



def makedir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def writeline(file, line):
    file.write(line + "\n")


if __name__ == '__main__':
    marlin = Repo("MarlinFirmware", "Marlin")
    # Text file with one commit sha per line.
    sp = SubjectParser("merge-diffs/variability-conflict-merges.txt")
    conflict_merges = sp.get_commits()

    git = Git(marlin)
    git.clone()

    for i, conflict_merge in enumerate(conflict_merges):
        print "{}/{} - {}".format(i+1, len(conflict_merges), conflict_merge)
        workspace = Workspace(conflict_merge, git)
        workspace.populate()
