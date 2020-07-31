from github import Github, ContentFile
from github.GithubException import UnknownObjectException
import argparse
import os

class GitHubDownloader:
    def __init__(self):
        self.repository = None
        self.selection = None
        self.github = Github()

        usage = "python .../github_downloader [-h] [-t TOKEN] [-u USER] [-p PASSWORD] repository selection"
        self.parser = argparse.ArgumentParser(description="download files or directory from github", usage=usage)
        self.parser_configuration()

        self.args = self.parser.parse_args()
        self.parser_verification()
        self.parser_parse()

        self.github_repo = None

    def parser_configuration(self):
        # Parser configuration
        self.parser.add_argument("repository", type=str, help="the repository from which you download the file/directory")
        self.parser.add_argument("selection", type=str, help="the file/directory to download")

        # TODO: add output
        # self.parser.parser.add_argument("-o", "--output")

        self.parser.add_argument("-t", "--token", type=str, help="token to use to download the file/directory")
        self.parser.add_argument("-u", "--user", type=str, help="user to use to download the file/directory")
        self.parser.add_argument("-p", "--password", type=str, help="password to use to download the file/directory")

    def parser_verification(self):
        # Parser verification
        if self.args.token and (self.args.user or self.args.password):
            self.parser.error("can't use token and user/password, please choose one or the other.")

        if self.args.token is None:
            if (self.args.user and self.args.password is None):
                self.parser.error("you must precise the password if you use the --user argument")
            if (self.args.user is None and self.args.password):
                self.parser.error("you must precise the user if you use the --password argument")

    def parser_parse(self):
        self.repository = self.args.repository
        self.selection = self.args.selection

        if self.args.token is not None:
            self.github = Github(self.args.token)
        elif self.args.user is not None and self.args.password is not None:
            self.github = Github(self.args.user, self.args.password)

    def write_file(self, content_file):
        try:
            with open(content_file.path, "wb") as f:
                f.write(content_file.decoded_content)
        except FileNotFoundError:
            self.create_parent_directory(content_file.path)
            with open(content_file.path, "wb") as f:
                f.write(content_file.decoded_content)

    def create_parent_directory(self, path):
        path_split = path.split('/')
        for iterator in range(1, len(path_split)):
            to_create = '/'.join(path_split[:iterator])
            os.mkdir(to_create)

    def normalize(self, content_files, path=""):
        to_return = []

        for content_file in content_files:
            if content_file.type == "dir":
                to_find = path + content_file.name
                new_path = "{}/".format(content_file.name)
                content_list = self.normalize(self.github_repo.get_contents(to_find), new_path)
                for f in content_list:
                    to_return.append(f)
            else:
                to_return.append(content_file)

        return to_return

    def normalize_nested_lists(self, content_files, path=""):
        for iterator in range(len(content_files)):
            if content_files[iterator].type == "dir":
                content_file = content_files[iterator]

                to_find = path + content_file.name
                new_path = "{}/".format(content_file.name)

                content_files[iterator] = self.normalize_nested_lists(self.github_repo.get_contents(to_find), new_path)

        return content_files

    def run(self):

        # Get the repository
        try:
            self.github_repo = self.github.get_repo(self.repository)
        except UnknownObjectException:
            print("Not found, try using owner/repository or verify that you have access to the repository.")
            exit(1)

        # Get the file or directory
        file_or_dir = self.github_repo.get_contents(self.selection)

        # Selection is file or directory
        if isinstance(file_or_dir, ContentFile.ContentFile):
            self.write_file(file_or_dir)
        else:
            my_dir = self.normalize(file_or_dir, "{}/".format(self.selection))
            for f in my_dir:
                self.write_file(f)

if __name__ == "__main__":
    github_downloader = GitHubDownloader()
    github_downloader.run()
