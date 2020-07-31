# Github Downloader

## Installation

Follow this procedure to install the github downloader tool:
- Clone this repository wherever you want
- cd into GitHubDownloader
- Create a python virtual environment with `python3 -m venv venv` (unix) or `python -m venv venv` (windows)
- Activate the virtual environment with `source ./venv/bin/activate` (unix) or `.\venv\Scripts\activate` (windows)
- Install the required libraries (contains flake8 and rope for development purposes) with `pip install -r requirements.txt`

You're all ready to go !

## Usage

To use this tool simply use :
`source ./venv/bin/activate` (unix) or `.\venv\Scripts\activate` (windows)

`python .../github_downloader your_args`

Here's the help page that you can find with the -h or --help arg :
```
github_downloader.py [-h] [-b BRANCH] [-t TOKEN] [-u USER] [-p PASSWORD]
                            repository selection

download files or directory from github

positional arguments:
  repository            the repository from which you download the file/directory
  selection             the file/directory to download

optional arguments:
  -h, --help            show this help message and exit
  -b BRANCH, --branch BRANCH
                        branch to download the file/directory from
  -t TOKEN, --token TOKEN
                        token to use to download the file/directory
  -u USER, --user USER  user to use to download the file/directory
  -p PASSWORD, --password PASSWORD
                        password to use to download the file/directory
```

## Warnings

There's a bandwidth limit with the github api so the script may stop working, use a vpn / proxy or just wait for a while.

This tool will write new file in your current directory, if a file happens to already exist, it will be overwritten so proceed carefully.

