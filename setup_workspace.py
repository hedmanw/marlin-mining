from subprocess import Popen, PIPE

workspace_dir = "merge_workspace"
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
    with open('README.txt', 'w') as f:
        f.write(merging_notice + "\n")
        f.write("-------\n")
        f.write("Conflicts:\n")
        f.write("\n".join(conflict_files))

    # grep -Pzo Marlin/Marlin.h -e "(?s)<<<<<<< HEAD.*if.*>>>>>>>"
    # grep -Pzo Marlin/Marlin_main.cpp -e "(?s)<<<<<<< HEAD.*?ifdef.*?>>>>>>>"
    # awk '/<<<<<<< HEAD/,/>>>>>>>/' Marlin/Marlin_main.cpp
    # TODO: pipe all files in merge_output into awk and then into grep(?)
    # TODO: split output on merge characters
    # TODO: trace back to original file in order to extract line numbers
    # TODO: write metadata (filename, line numbers) and code to files

    # TODO: manually check how the merge was resolved


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


def sample_merge(files):
    merge_limits = map(lambda x: awk(x), files)
    files_to_conflicts = {}
    for index, source_file in enumerate(files):
        files_to_conflicts[source_file] = merge_limits[index].split(">>>>>>>")

    return files_to_conflicts


def print_samples(files_with_conflicts):
    counter = 0
    for source_file in files_with_conflicts:
        all_conflicts = files_with_conflicts[source_file]
        for conflict in all_conflicts:
            with open("{}_{}".format(source_file[source_file.index('/')+1:], counter), 'w') as f:
                f.write("// EXCERPT FROM {}\n\n".format(source_file))
                f.write(conflict + "\n")
            counter += 1


def awk(file_path):
    awk_process = Popen(["awk", "/<<<<<<< HEAD/,/>>>>>>>/", file_path], cwd=workspace_dir, stdout=PIPE, stderr=PIPE)
    stdout, stderr = awk_process.communicate()
    awk_process.wait()
    print stderr
    return stdout


def git_process(args, cwd=None):
    args.insert(0, "git")
    process = Popen(args, cwd=cwd, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    return process, stdout, stderr


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
    sample = sample_merge(conflicts_sample.splitlines())
    print_samples(sample)
    #print awk("Marlin/Marlin_main.cpp")
