#!/usr/bin/env python

from subprocess import Popen, PIPE
from shutil import copyfile

import os, re

temp_dir = "/tmp/"


class Repo:
    def __init__(self, owner, repo_name):
        self.owner = owner
        self.repo_name = repo_name

    def clone_url(self):
        return "git@github.com:{}/{}".format(self.owner, self.repo_name)

    def __repr__(self):
        return self.owner + "/" + self.repo_name


class PullRequestMerge:
    def __init__(self, sha, pr_number, file_name):
        self.sha = sha
        self.pr_number = pr_number
        self.file_name = file_name

    def __repr__(self):
        return "PR#" + self.pr_number + "#" + self.sha


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
        return stdout

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
    def __init__(self, dir_name):
        self.dir_name = dir_name

    def get_commits(self):
        files = os.listdir(self.dir_name)
        return map(lambda _: self.read_file(_), files)

    def read_file(self, file_name):
        with open(os.path.join(self.dir_name, file_name), "r") as diff_file:
            contents = diff_file.readlines()
            pr_number = re.search(r"#\d*", contents[5]).group(0)[1:]
            return PullRequestMerge(contents[0][7:-1], pr_number, file_name)


class Workspace:
    def __init__(self, pull_request, git):
        self.pull_request = pull_request
        self.workspace_dir = pull_request.sha[:7]
        self.git = git

    def populate(self):
        (valid, commit_ref) = self.get_parents()
        if valid:
            self.create()
            self.checkout_and_copy(commit_ref.sha, "result")
            self.checkout_and_copy(commit_ref.first_parent_sha, "mainline")
            self.checkout_and_copy(commit_ref.second_parent_sha, "clone")
            self.log_commit(commit_ref)
        else:
            print "-- Commit {} was invalid.".format(self.pull_request.sha)

    def log_commit(self, commit_ref):
        def link_to_commit(commit):
            return "https://github.com/MarlinFirmware/Marlin/commit/{}".format(commit)

        def link_to_pr(pr):
            return "https://github.com/MarlinFirmware/Marlin/pull/{}".format(pr)

        print "Writing log for {}".format(self.workspace_dir)
        with open(os.path.join(self.workspace_dir, "README.md"), 'w') as x:
            writeline(x, "# " + self.workspace_dir)
            writeline(x, "- Pull request: [#{}]({})".format(self.pull_request.pr_number, link_to_pr(self.pull_request.pr_number)))
            writeline(x, "- Result commit: [{}]({})".format(commit_ref.sha, link_to_commit(commit_ref.sha)))
            writeline(x, "- First parent (mainline): [{}]({})".format(commit_ref.first_parent_sha, link_to_commit(commit_ref.first_parent_sha)))
            writeline(x, "- Second parent (clone): [{}]({})".format(commit_ref.second_parent_sha, link_to_commit(commit_ref.second_parent_sha)))


    def checkout_and_copy(self, sha, prefix):
        self.git.checkout(sha)
        file_name = "Marlin_main.cpp"
        copyfile(os.path.join(temp_dir, self.git.repo.repo_name, "Marlin", file_name), os.path.join(self.workspace_dir, "{}_{}".format(prefix, file_name)))

    def create(self):
        makedir(self.workspace_dir)

    def get_parents(self):
        parent_shas = self.git.get_commit_parent(self.pull_request.sha).strip().split(" ")
        return len(parent_shas) == 2, Commit(self.pull_request.sha, parent_shas[0], parent_shas[1])


def makedir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def writeline(file, line):
    file.write(line + "\n")


if __name__ == '__main__':
    marlin = Repo("MarlinFirmware", "Marlin")
    sp = SubjectParser("first-parent-merge-diffs/pr_Marlin_main")
    #pull_request_merges = sp.get_commits()

    git = Git(marlin)
    git.clone()

    Workspace(sp.read_file("mm291.diff"), git).populate()

    # for i, pull_request in enumerate(pull_request_merges):
    #     print "{}/{} - {}".format(i, len(pull_request_merges), pull_request.file_name)
    #     workspace = Workspace(pull_request, git)
    #     workspace.populate()
