import requests
import os
import subprocess
import sys

URL = "https://api.github.com/repos/nikil-sigmoid/authenticate_demo/pulls/1/files"
PARAMS= {"base": "main"}
HEADERS = {}
HEADERS["Authorization"] = f"Bearer {sys.argv[1]}"

def get_closed_pr_list():
    data = requests.get(url=URL, params=PARAMS, headers=HEADERS)
    return data.json()


def main():
    closed_pr_list = get_closed_pr_list() 

    num = len(closed_pr_list)
    print(closed_pr_list)


if __name__ == "__main__":
    main()
