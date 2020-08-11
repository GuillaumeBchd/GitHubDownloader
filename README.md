# Github Downloader

A simple tool to download file or directory from github repository via the github api.

## Installation

You need to have python3 and the library requests installed.

Follow this procedure to install the github downloader tool:
- Clone this repository wherever you want
- cd into GitHubDownloader

Or to use it on your linux system :
```
cd /opt
git clone https://github.com/GuillaumeBchd/GitHubDownloader.git
cd /usr/local/bin
ln /opt/GitHubDownloader/github_downloader/github_downloader.py .
chmod +x github_downloader.py
```

You're all ready to go !

## Usage

If you've followed the linux system installation guide you can use it directly with `github_downloader.py your_args`

Here's the help page that you can find with the -h or --help arg :
```
usage: github_downloader.py [-h] [-b BRANCH] [-t TOKEN] repository selection

download files or directory from github

positional arguments:
  repository            format : owner/repository, the repository from which you download the file/directory
  selection             the file/directory to download

optional arguments:
  -h, --help            show this help message and exit
  -b BRANCH, --branch BRANCH
                        branch to download the file/directory from
  -t TOKEN, --token TOKEN
                        token to use to download the file/directory
```

## Warnings

There's a bandwidth limit with the github api so the script may stop working, use a vpn / proxy or just wait for a while.

This tool will write new file in your current directory, if a file happens to already exist, it will be overwritten so proceed carefully.

