#!/usr/bin/env python

import sys
from subprocess import Popen, PIPE
import os
import csv
import re

FILE_NAME = "chunks.csv"


def main(mainline_src, fork_src, files_list):
    with open(files_list, 'r') as files_to_read:
        for file_src in files_to_read.readlines():
            file_name = file_src.strip()
            diff_file(file_name.replace(fork_src, mainline_src), file_name)


def diff_file(ml_file, fork_file):
    cwd = os.getcwd()
    _, stdout, stderr = run(['diff', os.path.join(cwd, ml_file), os.path.join(cwd, fork_file)])
    if stdout:
        added = len(re.findall(r"^\d+a", stdout, re.MULTILINE))
        deleted = len(re.findall(r"^\d+(,\d+)?d", stdout, re.MULTILINE))
        modified = len(re.findall(r"^\d+(,\d+)?c", stdout, re.MULTILINE))
        print "{}: a={}, d={}, c={}".format(ml_file, added, deleted, modified)
        append_to_csv(ml_file, fork_file, added, deleted, modified)



def run(args, cwd=None):
    process = Popen(args, cwd=cwd, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    process.wait()
    return process, stdout, stderr


def append_to_csv(ml_src, fork_src, added, deleted, changed):
    with open(FILE_NAME, 'a') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([
            ml_src,
            fork_src,
            added,
            deleted,
            changed
        ])

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], "/home/wilhelm/downloads/busybox/files_all.txt")