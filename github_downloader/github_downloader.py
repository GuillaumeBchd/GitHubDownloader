#!/usr/bin/env python3

import argparse
import os
import requests
import base64

class GitHubDownloader:
    def __init__(self):
        self.repository = None
        self.selection = None
        self.branch = "master"
        self.token = None

        self.parser = argparse.ArgumentParser(description="download files or directory from github", prog="github_downloader.py")
        self.parser_configuration()

        self.args = self.parser.parse_args()
        self.parser_parse()

        self.github_repo = None

    def parser_configuration(self):
        # Parser configuration
        self.parser.add_argument("repository", type=str, help="owner/repository, the repository from which you download the file/directory")
        self.parser.add_argument("selection", type=str, help="the file/directory to download")

        # TODO: add output
        # self.parser.parser.add_argument("-o", "--output")

        self.parser.add_argument("-b", "--branch", type=str, help="branch to download the file/directory from")
        self.parser.add_argument("-t", "--token", type=str, help="token to use to download the file/directory")

    def parser_parse(self):
        self.repository = self.args.repository
        self.selection = self.args.selection

        if self.args.branch is not None:
            self.branch = self.args.branch

        if self.args.token is not None:
            self.token = self.args.token

    def write_file(self, path, content):
        try:
            with open(path, "wb") as f:
                f.write(content)
        except FileNotFoundError:
            self.create_parent_directory(path)
            with open(path, "wb") as f:
                f.write(content)

    def create_parent_directory(self, path):
        path_split = path.split('/')
        for iterator in range(1, len(path_split)):
            to_create = '/'.join(path_split[:iterator])
            os.mkdir(to_create)

    def get_tree(self, sha):
        header = None
        if self.token is not None:
            header = {"Authorization": "token {}".format(self.token)}

        url = "https://api.github.com/repos/{}/git/trees/{}".format(self.repository, sha)
        response = requests.get(url, headers=header)

        try:
            return response.json()["tree"]
        except KeyError:
            return None

    def get_sha(self, tree, path):
        for elem in tree:
            if elem["path"] == path:
                return elem["sha"], elem["type"]

    def get_blob(self, sha):
        header = None
        if self.token is not None:
            header = {"Authorization": "token {}".format(self.token)}

        url = "https://api.github.com/repos/{}/git/blobs/{}".format(self.repository, sha)

        response = requests.get(url, headers=header)
        return base64.b64decode(response.json()["content"])

    def explore_tree(self, sha, base_path):
        tree = self.get_tree(sha)
        for elem in tree:
            if elem["type"] == "tree":
                self.explore_tree(elem["sha"], base_path + "/" + elem["path"])
            else:
                path = base_path + "/" + elem["path"]
                self.download(elem["sha"], path)

    def download(self, sha, path):
        content = self.get_blob(sha)
        self.write_file(path, content)

    def run(self):
        selection_split = self.selection.split('/')

        elem_sha = self.branch
        for elem in selection_split:
            elem_sha, elem_type = self.get_sha(self.get_tree(elem_sha), elem)

        if elem_type == "blob":
            self.download(elem_sha, self.selection)

        elif elem_type == "tree":
            self.explore_tree(elem_sha, self.selection)

if __name__ == "__main__":
    github_downloader = GitHubDownloader()
    github_downloader.run()
