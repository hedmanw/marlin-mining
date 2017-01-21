from subprocess import Popen, PIPE

import os

workspace_dir = "merge_workspace"
excerpts_dir = "merge_excerpts"
dry_run = False


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
    with open(excerpts_dir + '/README.txt', 'w') as f:
        f.write(merging_notice + "\n")
        f.write("-------\n")
        f.write("Conflicts:\n")
        f.write("\n".join(conflict_files))

    # TODO: trace back to original file in order to extract line numbers
    # TODO: write metadata (filename, line numbers) and code to files



def clone(repository):
    if not dry_run:
        github_url = repository.clone_url()
        process, _, _ = git_process(["clone", github_url, workspace_dir])
        process.wait()


def checkout(commit):
    if not dry_run:
        process, _, _ = git_process(["checkout", commit.hash], cwd=workspace_dir)
        process.wait()


def merge(commit):
    if not dry_run:
        github_url = commit.repo.clone_url()
        merge_process, stdout, stderr = git_process(["pull", github_url, commit.hash], cwd=workspace_dir)
        merge_process.wait()
        return stdout
    return None


def get_merge_excerpts(file_names):
    all_conflicts = []

    for file_name in file_names:
        file_conflicts = awk(file_name).split("<<<<<<<")[1:]
        for file_conflict in file_conflicts:
            all_conflicts.append(Conflict(file_name, file_conflict, 0, 0))

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


def store_parents(conflicts):
    pass


def store_result(conflicts):
    pass

def awk(file_path):
    awk_process = Popen(["awk", "/<<<<<<< HEAD/,/>>>>>>>/", file_path], cwd=workspace_dir, stdout=PIPE, stderr=PIPE)
    stdout, stderr = awk_process.communicate()
    awk_process.wait()
    return stdout


def git_process(args, cwd=None):
    args.insert(0, "git")
    process = Popen(args, cwd=cwd, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    return process, stdout, stderr


def makedir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

def format_conflicts(merge_text):
    merge_lines = merge_text.splitlines()
    only_conflict_lines = lambda x: x.startswith("CONFLICT (content):")
    relevant_files = lambda x: not ("README.md" in x or ".gitignore" in x)
    only_filenames = lambda x: x[len("CONFLICT (content): Merge conflict in "):]
    return map(only_filenames, filter(relevant_files, filter(only_conflict_lines, merge_lines)))

conflicts_sample = """Marlin/ultralcd_implementation_hitachi_HD44780.h
Marlin/ultralcd.cpp
Marlin/pins.h
Marlin/language.h
Marlin/Marlin_main.cpp
Marlin/Configuration.h"""


if __name__ == '__main__':
    base_repo = Repo("fsantini", "solidoodle2-marlin")
    base = Commit(base_repo, "3c0afb4")
    result = Commit(base_repo, "87b8062")

    integration_repo = Repo("MarlinFirmware", "Marlin")
    integration = Commit(integration_repo, "d75cd69de43afada517557b63a6c693eaa828580")
    #main(base, integration, result)
    conflict_files = conflicts_sample.splitlines()
    sample = get_merge_excerpts(conflict_files)
    store_merge_excerpts(sample)
    store_parents(conflict_files)
    store_result(conflict_files)
    #print awk("Marlin/Marlin_main.cpp")
