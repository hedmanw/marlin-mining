#!/usr/bin/env python

from subprocess import Popen, PIPE
from shutil import copyfile

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
            self.checkout_and_copy(commit_ref.sha, "result")
            self.checkout_and_copy(commit_ref.first_parent_sha, "base")
            self.checkout_and_copy(commit_ref.second_parent_sha, "remote")
            self.log_commit(commit_ref)
        else:
            print "-- Commit {} was invalid.".format(self.conflict_merge)

    def log_commit(self, commit_ref):
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

    def checkout_and_copy(self, sha, prefix):
        self.git.checkout(sha)
        file_name = "Marlin_main.cpp"
        copyfile(os.path.join(temp_dir, self.git.repo.repo_name, "Marlin", file_name), os.path.join(self.workspace_dir, "{}_{}".format(prefix, file_name)))

    def create(self):
        makedir(self.workspace_dir)

    def get_parents(self):
        parent_shas = self.git.get_commit_parent(self.conflict_merge).strip().split(" ")
        return len(parent_shas) == 2, Commit(self.conflict_merge, parent_shas[0], parent_shas[1])


def makedir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def writeline(file, line):
    file.write(line + "\n")


if __name__ == '__main__':
    marlin = Repo("fmalpartida", "Marlin")
    # Text file with one commit sha per line.
    sp = SubjectParser("FILENAME")
    conflict_merges = sp.get_commits()

    git = Git(marlin)
    git.clone()

    for i, conflict_merge in enumerate(conflict_merges):
        print "{}/{} - {}".format(i+1, len(conflict_merges), conflict_merge)
        workspace = Workspace(conflict_merge, git)
        workspace.populate()
