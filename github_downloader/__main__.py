try:
    from github_downloader import GitHubDownloader
except ImportError:
    from github_downloader.github_downloader import GitHubDownloader

if __name__ == "__main__":
    github_downloader = GitHubDownloader()
    github_downloader.run()
