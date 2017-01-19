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
    # clone(base.repo)

    print "Checking out {}".format(base.hash)
    checkout(base)

    merging_notice = "Merging {} with {}".format(base, integration)
    print merging_notice
    merge(integration)

    print "Recorded merging status in README"
    # TODO: Write to file


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
        print stderr


def git_process(args, cwd=None):
    args.insert(0, "git")
    process = Popen(args, cwd=cwd, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    return process, stdout, stderr

merge_output = """From github.com:MarlinFirmware/Marlin
 * branch            d75cd69de43afada517557b63a6c693eaa828580 -> FETCH_HEAD
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Auto-merging Marlin/ultralcd_implementation_hitachi_HD44780.h
CONFLICT (content): Merge conflict in Marlin/ultralcd_implementation_hitachi_HD44780.h
Auto-merging Marlin/ultralcd.cpp
CONFLICT (content): Merge conflict in Marlin/ultralcd.cpp
Auto-merging Marlin/thermistortables.h
Auto-merging Marlin/temperature.h
Auto-merging Marlin/temperature.cpp
Auto-merging Marlin/planner.cpp
Auto-merging Marlin/pins.h
CONFLICT (content): Merge conflict in Marlin/pins.h
Auto-merging Marlin/language.h
CONFLICT (content): Merge conflict in Marlin/language.h
Removing Marlin/createTemperatureLookupMarlin.py
Auto-merging Marlin/Marlin_main.cpp
CONFLICT (content): Merge conflict in Marlin/Marlin_main.cpp
Auto-merging Marlin/Configuration_adv.h
Auto-merging Marlin/Configuration.h
CONFLICT (content): Merge conflict in Marlin/Configuration.h
Removing Marlin/COPYING
Auto-merging .gitignore
CONFLICT (content): Merge conflict in .gitignore
Automatic merge failed; fix conflicts and then commit the result"""

if __name__ == '__main__':
    base_repo = Repo("fsantini", "solidoodle2-marlin")
    base = Commit(base_repo, "3c0afb4")
    result = Commit(base_repo, "87b8062")

    integration_repo = Repo("MarlinFirmware", "Marlin")
    integration = Commit(integration_repo, "d75cd69de43afada517557b63a6c693eaa828580")
    main(base, integration, result)