from subprocess import Popen, PIPE
from shutil import copyfile

import os

workspace_dir = "merge_workspace"
excerpts_dir = "merge_excerpts"
content_dir = "whole_files"
dry_run = False


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


def main(base, integration, result):
    print "Cloning {}...".format(base.repo)
    clone(base.repo)

    print "Checking out {}".format(base.hash)
    checkout(base)

    merging_notice = "Merging {} with {}".format(base, integration)
    print merging_notice
    merge_output = merge(integration)

    print "Recorded merging status in README.txt"
    conflict_files = format_conflicts(merge_output)

    makedir(excerpts_dir)
    commit_url = "https://github.com/{}/{}/commit/".format(base.repo.owner, base.repo.repo_name)
    with open('README.txt', 'w') as f:
        def write(line):
            writeline(f, line)
        write(merging_notice)
        write("First parent:  {}{}".format(commit_url, base.hash))
        write("Second parent: {}{}".format(commit_url, integration.hash))
        write("Outcome:       {}{}".format(commit_url, result.hash))
        write("-------")
        write("Conflicts:")
        write("\n".join(conflict_files))

    #conflict_files = conflicts_sample.splitlines()
    print "Reading conflicts."
    conflicts = get_merge_excerpts(conflict_files)
    #conflicts = map(lambda x: Conflict(x, "", 0, 0), conflict_files)
    merge_instance = Merge(base, integration, result, conflicts)
    print "Storing excerpts of conflicts in merge_excerpts/"
    store_merge_excerpts(conflicts)
    print "Storing whole files in whole_files/"
    store_commit_contents(merge_instance)


def clone(repository):
    if not dry_run:
        github_url = repository.clone_url()
        process, _, _ = git_process(["clone", github_url, workspace_dir])


def checkout(commit):
    process, stdout, stderr = git_process(["checkout", commit.hash], cwd=workspace_dir)


def merge(commit):
    if not dry_run:
        github_url = commit.repo.clone_url()
        merge_process, stdout, stderr = git_process(["pull", github_url, commit.hash], cwd=workspace_dir)
        return stdout
    return None


def abort_merge():
    git_process(["merge", "--abort"], cwd=workspace_dir)


def get_merge_excerpts(file_names):
    all_conflicts = []

    for file_name in file_names:
        file_conflicts = awk(file_name).split("<<<<<<<")[1:]
        for file_conflict in file_conflicts:
            all_conflicts.append(Conflict(file_name, file_conflict, 0, 0))

    print "  Storing snapshots of the merge (merge) in {}/".format(content_dir)
    copy_example_files(None, "merge", all_conflicts)
    abort_merge()

    return all_conflicts


def store_merge_excerpts(conflicts):
    counter = 0
    for conflict in conflicts:
        source_file = conflict.filename
        qualified_source_name = source_file[source_file.index('/') + 1:]
        makedir(excerpts_dir)
        with open("{}/{}_{}".format(excerpts_dir, qualified_source_name, counter), 'w') as f:
            f.write("// EXCERPT FROM MERGE  {}\n\n".format(source_file))
            f.write("<<<<<<<" + conflict.content + "\n")
        counter += 1


def store_commit_contents(merge):
    print "  Storing files in first parent (base) #{}".format(merge.base_commit.hash)
    copy_example_files(merge.base_commit, "base", merge.conflicts)
    print "  Storing files in second parent (remote) #{}".format(merge.integration_commit.hash)
    copy_example_files(merge.integration_commit, "remote", merge.conflicts)
    print "  Storing files in outcome (result) #{}".format(merge.result.hash)
    copy_example_files(merge.result, "result", merge.conflicts)


def copy_example_files(commit, prefix, conflicts):
    makedir(content_dir)
    if commit:
        checkout(commit)
    for conflict in conflicts:
        source_file = conflict.filename
        qualified_source_name = source_file[source_file.index('/') + 1:]
        dir_source_file = workspace_dir + "/" + source_file
        dir_target_file = content_dir + "/" + prefix + "_" + qualified_source_name
        #print "Copying {} to {}.".format(dir_source_file, dir_target_file)
        copyfile(dir_source_file, dir_target_file)


def awk(file_path):
    awk_process = Popen(["awk", "/<<<<<<< HEAD/,/>>>>>>>/", file_path], cwd=workspace_dir, stdout=PIPE, stderr=PIPE)
    stdout, stderr = awk_process.communicate()
    awk_process.wait()
    return stdout


def git_process(args, cwd=None):
    args.insert(0, "git")
    process = Popen(args, cwd=cwd, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    process.wait()
    return process, stdout, stderr


def makedir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def writeline(file, line):
    file.write(line + "\n")

def format_conflicts(merge_text):
    merge_lines = merge_text.splitlines()
    only_conflict_lines = lambda x: x.startswith("CONFLICT (content):")
    relevant_files = lambda x: not ("README.md" in x or ".gitignore" in x)
    only_filenames = lambda x: x[len("CONFLICT (content): Merge conflict in "):]
    return map(only_filenames, filter(relevant_files, filter(only_conflict_lines, merge_lines)))


if __name__ == '__main__':
    base_repo = Repo("MarlinFirmware", "Marlin")
    base = Commit(base_repo, "48b1c3822ffaff054b99d17df5c38f386e577c5b")
    result = Commit(base_repo, "ea10601406dd24dd3e3bef3ec22319f73034fbf6")
    integration_repo = Repo("MarlinFirmware", "Marlin")
    integration = Commit(integration_repo, "cb02bc6db458bde59ddbf8ef37356a3eb5c0f4a8")

    main(base, integration, result)

