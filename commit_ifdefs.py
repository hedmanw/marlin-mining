#!/usr/bin/env python

import csv, os
from subprocess import Popen, PIPE

FILE_NAME = 'merge-ifdef-stats.csv'


def main(commits_path, diffs_directory, append=True):
    if not append:
        write_commit_csv_heading()

    for sha in list_commits(commits_path):
        get_commit(sha, diffs_directory)
    # get_commit("6ae7f7870d8ff09d99fdf7ed1dc64a6f727020ce", diffs_directory)
    # get_commit("ffe0df4b364f9100f20b76c59cbdcaffd2b785e5", diffs_directory)


def list_commits(path):
    with open(path, 'r') as commits_file:
        return map(lambda x: x.strip(), commits_file.readlines())


def get_commit(sha, directory):
    # if file doesn't exist, write 0.
    commit_file = os.path.join(directory, "{}.diff".format(sha))
    if not os.path.exists(commit_file):
        append_commit_json_to_csv(sha, Variability(0, 0, 0, 0, 0))
    else:
        grep = Grep(directory, commit_file, "\s*#((el)?if((n?)def| ((not )?defined)|(EN|DIS)ABLED))")
        changed_grep = Grep(directory, commit_file, "^-")
        added_content, added_count = grep.grep_added()
        deleted_content, deleted_count = grep.grep_removed()
        changed = count_changed(added_content, deleted_content, changed_grep)
        variability = Variability(added_count, deleted_count, changed, 0, 0)
        # print variability
        append_commit_json_to_csv(sha, variability)


def count_changed(added_ifdefs, deleted_ifdefs, changed_grep):
    added_values = added_ifdefs.splitlines()
    deleted_ifdefs_text_values = deleted_ifdefs.splitlines()
    deleted_lines = changed_grep.grep("").splitlines()
    ifdef_changes = 0
    if deleted_lines == 0:
        return 0
    for line_number, line in enumerate(deleted_lines):
        # text_value = line.split(':')[1]
        # print text_value
        if line in deleted_ifdefs_text_values: # This deleted block begins with an ifdef
            # Iterate until end of block, if next line is in added_ifdefs, we have a match
            block_index = line_number
            origin_line_number = int(line.split(':')[0])
            while block_index < len(deleted_lines)-1 and int(deleted_lines[block_index+1].split(':')[0]) == int(deleted_lines[block_index].split(':')[0])+1:
                block_index += 1
            target_line_number = "{}:+".format(origin_line_number + (block_index - line_number) + 1)
            # if origin_line_number == 1066:
                # print "next: {}".format(deleted_lines[block_index+1].split(':')[0])
                # print "original: {}, block_index: {}, line_number: {}, target:: {}".format(origin_line_number, block_index, line_number, target_line_number)
            if reduce(lambda acc, value: acc or value.startswith(target_line_number), added_values, False):
                # print "{}: {} :: EXPECTS: {}".format(line_number, line, target_line_number)
                ifdef_changes += 1

    return ifdef_changes


class Grep:
    def __init__(self, directory, filename, regex):
        self.directory = directory
        self.filename = filename
        self.regex = regex

    def grep_added(self):
        output = self.grep('\+')
        return output, self.count(output)

    def grep_removed(self):
        output = self.grep('-')
        return output, self.count(output)

    def count(self, lines):
        return len(lines.splitlines())

    def grep(self, line_prefix):
        process = Popen(["grep", self.filename, "-n", "-E", "-e", line_prefix + self.regex], cwd=self.directory, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        if len(stderr) > 0:
            raise ValueError(self.filename)
        process.wait()
        return stdout


class Variability:
    def __init__(self, added_ifdefs, deleted_ifdefs, changed_ifdefs, added_ifdefs_w_else, deleted_ifdefs_w_else):
        self.added_ifdefs = added_ifdefs
        self.deleted_ifdefs = deleted_ifdefs
        self.changed_ifdefs = changed_ifdefs
        self.added_ifdefs_w_else = added_ifdefs_w_else
        self.deleted_ifdefs_w_else = deleted_ifdefs_w_else

    def __repr__(self):
        return "+{}, -{}, ={}".format(self.added_ifdefs, self.deleted_ifdefs, self.changed_ifdefs)

def write_commit_csv_heading():
    with open(FILE_NAME, 'w') as csv_file:
        csv.writer(csv_file).writerow([
            "sha",
            "#added-ifdefs",
            "#deleted-ifdefs",
            "#changed-ifdefs",
            "#added-ifdefs_w_else",
            "#deleted-ifdefs_w_else",
        ])


def append_commit_json_to_csv(commit, variability):
    with open(FILE_NAME, 'a') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([
            commit,
            variability.added_ifdefs,
            variability.deleted_ifdefs,
            variability.changed_ifdefs,
            variability.added_ifdefs_w_else,
            variability.deleted_ifdefs_w_else
        ])

if __name__ == '__main__':
    main("COMMITS FILE",
         "DIFFS DIR", False)
