import requests
import os
import subprocess
import sys
from datetime import datetime
URL = "https://api.github.com/repos/nikil-sigmoid/test_github_actions/pulls?state=closed"
PARAMS= {"base": sys.argv[1]}


def sort_dates(closed_dates):
    closed_dates.sort()
    print(closed_dates)


def str_to_datetime(closed_dates):
    for date in closed_dates:
        date = datetime.strptime(date,'%Y-%m-%dT%H:%M:%SZ')


def get_closed_pr_list():
    data = requests.get(url=URL, params=PARAMS)
    return data.json()


def main():
    closed_pr_list = get_closed_pr_list() 

    print(closed_pr_list[0])
    num = len(closed_pr_list)
    os.environ['INITIAL_SHA'] = closed_pr_list[0]["merge_commit_sha"]
    os.environ['FINAL_SHA'] = closed_pr_list[1]["merge_commit_sha"]

    for item in range(0, 5):
        print(closed_pr_list[item]["url"])
        print(closed_pr_list[item]["number"])
        print(closed_pr_list[item]["merged_at"])
        print(closed_pr_list[item]["merge_commit_sha"])
        print()

    print()
    print(f"{os.environ['INITIAL_SHA']},{os.environ['FINAL_SHA']}")


if __name__ == "__main__":
    main()





