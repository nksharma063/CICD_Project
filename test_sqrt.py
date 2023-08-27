import pytest, sys
from sqrt import *
import json
import subprocess
from dotenv import load_dotenv

# loading the envionment variables
load_dotenv()

#decalering the global variables
owner = 'nksharma063'
repo = 'CICD_Project'
token = os.environ['GIT_TOKEN']
auth_token = os.environ['GIT_AUTH_TOKEN']


#Using curl for most of thing as request process was already figured out
#Fetching the latest commit-sha, message or comment and commit_message to forward the success status and commit Id to merge with dep branch.

commits = subprocess.check_output(['curl', '-L'  , '-H' ,'Accept: application/vnd.github+json',   '-H', 'token',   '-H', 'X-GitHub-Api-Version: 2022-11-28', f'https://api.github.com/repos/{owner}/{repo}/commits?sha=dev'])
commits = json.loads(commits.decode('utf-8'))
COMMITID = commits[0]['sha']
# COMMITID_LIST = list(COMMITID)
# print(COMMITID_LIST[0:], type(COMMITID))

#fetching the message actually first index of message for further processing
commit_message = commits[0]['commit']['message']
commit_message = commit_message.split(' ')
first_commit_message_index_value = commit_message[0].lower()

#gettings the commentscomments
comments = subprocess.check_output(['curl', '-L'  , '-H' ,'Accept: application/vnd.github+json',   '-H', 'token',   '-H', 'X-GitHub-Api-Version: 2022-11-28',   f'https://api.github.com/repos/{owner}/{repo}/commits/{COMMITID}/comments'])
comments = json.loads(comments.decode('utf-8'))
comments = comments[0]['body']
comments = comments.split(':')
first_Comment_index_value = comments[0].lower()

# if commit_message[0].lower() == 'add' and comments[0].lower() == 'done':
    # Reading existing commit ids from file
with open('commits.txt', 'r') as f:
    existing_commit_ids = f.read().splitlines()

    # Writing new commit id to file if conditions are met
if first_commit_message_index_value == 'add' and first_Comment_index_value == 'done':
    if COMMITID not in existing_commit_ids:
        with open('commits.txt', 'rw+') as f:
            f.write(COMMITID + '\n')
            commit_ids = f.read().splitlines()
            for commit_id in commit_ids:
                os.system(f'git cherry-pick {commit_id}')
     
# #Setting test scripts 
# def test_hello():
#      a = hello()
#      assert a == "hi breakout 4"

# if __name__ == "__main__":
#     exit_code = pytest.main()
#     test_passed = (exit_code == 0)
#     if test_passed == True:


# #Setting the status of commit ID fetched if test cases are passed to sucess using POST request
# # Set the status information
# state = 'success'
# context = 'continuous-integration/jenkins'
# description = 'The build succeeded!'

# # POST the commit status to "Sucess"
# cmd = ['curl', '-X', 'POST', '-H', f'Authorization: Bearer {auth_token}', '-H', 'Content-Type: application/json', '-d', f'{{"state":"{state}", "context":"{context}", "description":"{description}"}}', f'https://api.github.com/repos/{owner}/{repo}/statuses/{COMMITID}']


# print(data_status)
#Will use for deployement merge 

# commits = subprocess.check_output(['curl', '-L'  , '-H' ,'Accept: application/vnd.github+json',   '-H', 'token',   '-H', 'X-GitHub-Api-Version: 2022-11-28',   f'https://api.github.com/repos/nksharma063/CICD_Project/commits/{COMMITID}/status'])

# data = json.loads(commits.decode('utf-8'))
# print(data['state'])


#     # result = (exit_code == 0)
#     # print(result)




"""

# Update the commit status
# data_status = subprocess.check_output(['curl', '-L', '-X', 'POST', '-H', 'Accept: application/vnd.github+json', '-H', f'Authorization: Bearer {auth_token}', f'https://api.github.com/repos/nksharma063/CICD_Project/statuses/{COMMITID}', '-d' , '-d', '{"state":"success","context":"continuous-integration/jenkins"}'])


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

Another rough work

# commit_data = commits.json()
# commit_ids = []
# for commit in commit_data:
#     commit_id = commit["sha"]
#     commit_ids.append(commit_id)

# print(commit_ids)

#print(comment["parents"]["sha"][0])
"""


