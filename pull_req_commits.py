#!/usr/bin/env python

import requests
import sys
from optparse import OptionParser

import csv
import re

FILE_NAME = 'pull-requests.csv'

repo_url = "https://api.github.com/repos/MarlinFirmware/Marlin/pulls"
token = "XXX"


def get_pull_requests(begin=1, clean=False):
    if clean:
        write_pull_req_csv_heading()

    json, next_page = fetch_pull_reqs(begin)
    get_commits_for_page(json)

    while next_page:
        json, next_page = fetch_pull_reqs(next_page)
        get_commits_for_page(json)


def fetch_pull_reqs(page):
    response = get(repo_url, {"state": "closed", "page": page})
    if response.status_code != 200:
        raise ValueError("At page {}, got: {}".format(page, response.text))

    links = build_link_navigation(response.headers['link'])

    next_page = links.get('next')
    last_page = links.get('last')
    print "Page: {}/{}, next: {}".format(page, last_page, next_page)
    return response.json(), next_page


def get_commits_for_page(page_json):
    for pr in page_json:
        get_commits_for_pr(pr["number"])

def get_commits_for_pr(pull_request):
    print "  Downloading PR#{}".format(pull_request)
    url = "{}/{}/commits".format(repo_url, pull_request)
    response = get(url)
    if response.status_code != 200:
        print("PR#{} : {} --- {}".format(pull_request, response.status_code, response.text))
    else:
        content_json = response.json()
        append_pull_req_json_to_csv(pull_request, content_json)


def build_link_navigation(links_header):
    split_links = links_header.split(",")
    links = {}
    for link_blob in split_links:
        m = re.match(r".*page=(\d+)>; rel=\"(\w*)\"", link_blob)
        page, rel = m.groups()
        links[rel] = page

    return links


def get(url, params=None):
    return requests.get(url, params, headers={'Authorization': 'token ' + token})


def write_pull_req_csv_heading():
    with open(FILE_NAME, 'w') as csv_file:
        csv.writer(csv_file).writerow([
            "id",
            "pr",
            "sha",
            "author",
            "committer",
            "mergemessage",
            "#parents",
            "url",
            "html"
        ])


def append_pull_req_json_to_csv(pull_request, json):
    with open(FILE_NAME, 'a') as csv_file:
        csv_writer = csv.writer(csv_file)
        for commit in json:
            author = commit.get("author") and commit.get("author").get("login")
            committer = commit.get("committer") and commit.get("committer").get("login")
            csv_writer.writerow([
                pull_request,
                "https://github.com/MarlinFirmware/Marlin/pull/{}".format(pull_request),
                commit["sha"],
                author,
                committer,
                "Merge" in commit["commit"]["message"],
                len(commit["parents"]),
                commit["url"],
                commit["html_url"]
            ])

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-c", action="store_true", dest="clean", default=False)
    (options, args) = parser.parse_args(sys.argv)
    begin_index = int(args[1])
    if begin_index > 0:
        get_pull_requests(begin_index, options.clean)
