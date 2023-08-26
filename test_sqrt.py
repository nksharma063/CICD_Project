import pytest, sys
from sqrt import *
import json
import subprocess
from dotenv import load_dotenv

load_dotenv()


token = os.environ['GIT_TOKEN']

commits = subprocess.check_output(['curl', '-L'  , '-H' ,'Accept: application/vnd.github+json',   '-H', 'token',   '-H', 'X-GitHub-Api-Version: 2022-11-28',   'https://api.github.com/repos/nksharma063/CICD_Project/commits?sha=dev'])

commits = json.loads(commits.decode('utf-8'))
COMMITID = commits[0]['sha']
print(COMMITID)

comments = subprocess.check_output(['curl', '-L'  , '-H' ,'Accept: application/vnd.github+json',   '-H', 'token',   '-H', 'X-GitHub-Api-Version: 2022-11-28',   f'https://api.github.com/repos/nksharma063/CICD_Project/commits/{COMMITID}/comments'])

comments = json.loads(comments.decode('utf-8'))
comments = comments[0]['body']

print(comments)



"""
Rough work

from datetime import datetime, timedelta

TOKEN = "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"
OWNER = "nksharma063"
REPO = "CICD_Project"
BRANCH = "dev"
SINCE = (datetime.utcnow() - timedelta(hours=2)).strftime("%Y-%m-%dT%H:%M:%SZ")

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28"
}

"""

"""
Another rough work

# commit_data = commits.json()
# commit_ids = []
# for commit in commit_data:
#     commit_id = commit["sha"]
#     commit_ids.append(commit_id)

# print(commit_ids)

"""



#print(comment["parents"]["sha"][0])
# def test_hello():
#     a = hello()
#     assert a == "hi breakout 4"

# def test_registration():
#     a = registration()
#     assert a == "This is registration page"

# if __name__ == "__main__":
#     exit_code = sys.exit(pytest.main(["-x", "test_sqrt.py"]))
#     # result = (exit_code == 0)
#     # print(result)

