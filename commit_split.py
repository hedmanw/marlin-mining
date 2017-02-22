#!/usr/bin/env python

import os

import re


class Splitter:
    def __init__(self, directory, full_file):
        self.directory = directory
        self.full_file = full_file

    def split(self):
        with open(self.full_file, 'r') as diff_file:
            lines = diff_file.readlines()
            current_commit_begin = 0
            current_sha = 0
            old_sha = 0
            for index in range(0, len(lines)):
                current_line = lines[index]
                m = re.match(r"^commit ([0-9a-f])", current_line)
                if m:
                    current_sha = current_line[7:47]
                    if index == 0:
                        old_sha = current_sha

                    current_is_from = current_line[54:61]
                    print "{}: {} (from {})".format(index, current_sha, current_is_from)
                    if self.is_first_parent(current_is_from, lines[index+1]) and index > 0:
                        self.write(old_sha, lines[current_commit_begin:index])
                        print "Wrote to file."
                        current_commit_begin = index
                        old_sha = current_sha

    def is_first_parent(self, current_is_from, next_line):
        first_parent_begins = next_line[7:14]

        return first_parent_begins == current_is_from

    def write(self, sha, lines):
        file_name = "{}.diff".format(sha)
        with open(os.path.join(self.directory, file_name), 'w') as commit_file:
            commit_file.writelines(lines)

if __name__ == '__main__':
    splitter = Splitter("DIRECTORY_TO_STORE_DIFFS_IN",
                        "OUTPUT_FROM_git_log")
    splitter.split()
