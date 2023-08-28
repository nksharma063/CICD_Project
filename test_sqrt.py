"""
This will bring the changes of the dev files to test branch so that tester can reveiew and make changes into the test script.
We can also modify this script to work for some timeline using time filter
We can alos modify this script to impor multiple new commits by adding , new file with read mode and then compare old commit with new.
We need to set certain standard for the process like Add and done will only happen when new commits or changes to exiting file happens and not to be used anywhere.
This scrpt will just bring the changes , "next script will run the test cases and send the status of those to along with commit ID to dep branch for further deply the html or some other file to nginx server
"""
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

def latestCommit():
    commits = subprocess.check_output(['curl', '-L'  , '-H' ,'Accept: application/vnd.github+json',   '-H', 'token',   '-H', 'X-GitHub-Api-Version: 2022-11-28', f'https://api.github.com/repos/{owner}/{repo}/commits?sha=dev'])
    commits = json.loads(commits.decode('utf-8'))
    COMMITID = commits[0]['sha']
    commit_message = commits[0]['commit']['message']
    commit_message = commit_message.split(' ')
    first_commit_message_index_value = commit_message[0].lower()
    return COMMITID, first_commit_message_index_value
# COMMITID_LIST = list(COMMITID)
# print(COMMITID_LIST[0:], type(COMMITID))

#fetching the message actually first index of message for further processing

#gettings the commentscomments

def commitCommentt():
    comments = subprocess.check_output(['curl', '-L'  , '-H' ,'Accept: application/vnd.github+json',   '-H', 'token',   '-H', 'X-GitHub-Api-Version: 2022-11-28',   f'https://api.github.com/repos/{owner}/{repo}/commits/{COMMITID}/comments'])
    comments = json.loads(comments.decode('utf-8'))
    comments = comments[0]['body']
    comments = comments.split(':')
    first_Comment_index_value = comments[0].lower()
    return first_Comment_index_value

# if commit_message[0].lower() == 'add' and comments[0].lower() == 'done':
    # Reading existing commit ids from file
    # Writing new commit id to file if conditions are met
    #any new commit introduced in the dev system, i will fetch those commits and changes into the files and bring them to test branch and i am not appending becasue i dont want to stoare the previous, like last in first out and process repeat
def bringTheFileToTest():
    first_commit_message_index_value,COMMITID = latestCommit()
    first_Comment_index_value = commitCommentt()
    if first_commit_message_index_value == 'add' and first_Comment_index_value == 'done':
        with open('commits.txt', 'w') as f:
            f.write(COMMITID + '\n')
        with open('commits.txt', 'r') as f:
            commit_ids = f.read().splitlines()
            for commit_id in commit_ids:
                os.system(f'git cherry-pick {commit_id}')

if __name__ == '__main__':
    bringTheFileToTest()