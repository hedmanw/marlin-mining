#!/usr/bin/env python

import requests

import csv

FILE_NAME = 'merge-stats.csv'

repo_url = "https://api.github.com/repos/MarlinFirmware/Marlin/commits/"
token = "XXX"


def main(path, append=True):
    if not append:
        write_commit_csv_heading()

    for sha in list_commits(path):
        get_commit(sha)


def list_commits(path):
    with open(path, 'r') as commits_file:
        return map(lambda x: x.strip(), commits_file.readlines())

def get_commit(sha):
    print "  Getting #{}".format(sha)
    url = "{}{}".format(repo_url, sha)
    response = get(url)
    if response.status_code != 200:
        print("MERGE#{} : {} --- {}".format(sha, response.status_code, response.text))
    else:
        content_json = response.json()
        append_commit_json_to_csv(sha, content_json)


def get(url, params=None):
    return requests.get(url, params, headers={'Authorization': 'token ' + token})


def write_commit_csv_heading():
    with open(FILE_NAME, 'w') as csv_file:
        csv.writer(csv_file).writerow([
            "sha",
            "kind",
            "#files",
            "#additions",
            "#deletions",
        ])


def append_commit_json_to_csv(commit, json):
    with open(FILE_NAME, 'a') as csv_file:
        kind = "regular"
        if ("Conflicts:" in json["commit"]["message"]):
            kind = "conflicts"
        if ("Merge pull request #" in json["commit"]["message"]):
            kind = "prmerge"
        if (len(json["files"]) == 0):
            kind = "nochanges"
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([
            commit,
            kind,
            len(json["files"]),
            json["stats"]["additions"],
            json["stats"]["deletions"],
        ])

if __name__ == '__main__':
    main("FILE_WITH_ONE_SHA_PER_LINE", False)
