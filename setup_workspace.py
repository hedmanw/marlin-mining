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
    with open('README.txt', 'w') as f:
        f.write(merging_notice + "\n")
        f.write("-------\n")
        f.write("Conflicts:\n")
        f.write("\n".join(format_conflicts(merge_output)))


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


if __name__ == '__main__':
    base_repo = Repo("fsantini", "solidoodle2-marlin")
    base = Commit(base_repo, "3c0afb4")
    result = Commit(base_repo, "87b8062")

    integration_repo = Repo("MarlinFirmware", "Marlin")
    integration = Commit(integration_repo, "d75cd69de43afada517557b63a6c693eaa828580")
    main(base, integration, result)
