#!/usr/bin/env python

import requests

import csv
import re

repo_url = "https://api.github.com/repos/mirror/busybox/forks"
token = ""

def get_fork_data():
    write_csv_heading()

    json, next_page = fetch_forks(1)
    append_json_to_csv(json)

    while next_page:
        json, next_page = fetch_forks(next_page)
        append_json_to_csv(json)


def fetch_forks(page):
    response = get(repo_url, {"page":page})
    if response.status_code != 200:
        raise ValueError("At page " + page + ", got: " + response.text)

    links = build_link_navigation(response.headers['link'])

    next_page = links.get('next')
    last_page = links.get('last')
    print "Page: {}/{}, next: {}".format(page, last_page, next_page)
    return response.json(), next_page

def get(url, params=None):
    return requests.get(url, params, headers={'Authorization': 'token ' + token})

def build_link_navigation(links_header):
    split_links = links_header.split(",")
    links = {}
    for link_blob in split_links:
        m = re.match(r".*page=(\d+)>; rel=\"(\w*)\"", link_blob)
        page, rel = m.groups()
        links[rel] = page

    return links


def write_csv_heading():
    with open('data.csv', 'w') as csv_file:
        csv.writer(csv_file).writerow([
            "full name",
            "url",
            "description",
            "size",
            "#stars",
            "#forks",
            "created at",
            "last updated",
            "last pushed",
            "clone url"
        ])


def append_json_to_csv(json):
    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.writer(csv_file)
        for repo in json:
            desc = repo["description"]
            csv_writer.writerow([
                repo["full_name"],
                repo["html_url"],
                desc.encode('utf-8') if desc else "",
                repo["size"],
                repo["stargazers_count"],
                repo["forks_count"],
                repo["created_at"],
                repo["updated_at"],
                repo["pushed_at"],
                repo["git_url"]
            ])


if __name__ == '__main__':
    get_fork_data()