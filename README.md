# Github Downloader

## Installation

Follow this procedure to install the github downloader tool:
- Clone this repository wherever you want
- cd into GitHubDownloader

You're all ready to go !

## Usage

To use this tool simply use :
`source ./venv/bin/activate` (unix) or `.\venv\Scripts\activate` (windows)

`python .../github_downloader your_args`

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

