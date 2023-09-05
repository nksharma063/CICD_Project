"""
This script brings the changes of the dev files to the test branch so that testers can review and make changes to the test script.
We can also modify this script to work for some timeline using a time filter.
We can also modify this script to import multiple new commits by adding a new file with read mode and then comparing old commits with new.
We need to set certain standards for the process, such as Add and Done will only happen when new commits or changes to existing files happen and not be used anywhere else.
This script will just bring the changes. The next script will run the test cases and send the status of those along with the commit ID to the dep branch for further deployment of the HTML or some other file to the Nginx server.
"""
import json
import os
import subprocess
from dotenv import load_dotenv
import logging

# Loading the environment variables
load_dotenv()

logging.basicConfig(filename="record_testsqrt.log", level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

# Declaring the global variables
owner = 'nksharma063'
repo = 'CICD_Project'
token = os.environ['GIT_TOKEN']
auth_token = os.environ['GIT_AUTH_TOKEN']

# Define commit messages
commit_message = "Automatic commit when bringing changes to the test branch and adding new commit to the commit id file"
commit_message_after_cherrypick = "Automatic commit after cherry-picking and pushing changes to the test branch"

# Using curl for most things as request process was already figured out
# Fetching the latest commit-sha, message or comment, and commit_message to forward the success status and commit ID to merge with dep branch.

# Function to fetch the latest commit ID and commit message from the dev branch
def latest_commit():
    try:
        """Fetches the latest commit ID and first word of commit message from dev branch"""
        commits = subprocess.check_output(['curl', '-L', '-H', 'Accept: application/vnd.github+json', '-H', 'token', '-H', 'X-GitHub-Api-Version: 2022-11-28', f'https://api.github.com/repos/{owner}/{repo}/commits?sha=dev'])
        commits = json.loads(commits.decode('utf-8'))
        commit_id = commits[0]['sha']
        print(commit_id)
        commit_message = commits[0]['commit']['message']
        first_word_of_commit_message = commit_message.split(' ')[0].lower()
        return commit_id, first_word_of_commit_message
    except Exception as e:
        logger.error(f"Something has happened in latest_comment function in test_sqrt.py file: {e}")
        return None, None

def commit_comment(commit_id):
    """Fetches the first word of comment from a given commit ID"""
    try:
        comments = subprocess.check_output(['curl', '-L', '-H', 'Accept: application/vnd.github+json', '-H', 'token', '-H', 'X-GitHub-Api-Version: 2022-11-28', f'https://api.github.com/repos/{owner}/{repo}/commits/{commit_id}/comments'])
        comments = json.loads(comments.decode('utf-8'))
        comment_body = comments[0]['body']
        first_word_of_comment = comment_body.split(':')[0].lower()
        return first_word_of_comment
    except Exception as e:
        logger.error(f"Something has happened in commit_comment function in test_sqrt.py file: {e} ")
        return None


def bring_changes_to_test():
    """Brings changes from dev branch to test branch if conditions are met"""
    commit_id, first_word_of_commit_message = latest_commit()
    first_word_of_comment = commit_comment(commit_id)
    try:
        if os.path.exists('commits.txt'):
            if first_word_of_comment == 'done':
                with open('commits.txt', 'w') as f:
                    f.write(commit_id + '\n')
                os.system('git stash')
                os.system('git checkout test -f')
                os.system('git fetch')
                os.system(' git add .')
                os.system(f"git commit -m \"{commit_message}\"")
                os.system("git push origin test")
        
                with open('commits.txt', 'r') as f:
                    commit_ids = f.read().splitlines()
                    for cid in commit_ids:
                        os.system(f'git cherry-pick {cid}')
                    os.system(' git add .')
                    os.system(f"git commit -m \"{commit_message_after_cherrypick}\"")
                    os.system("git push origin test")
        else:
            if first_word_of_comment == 'done':
                with open('commits.txt', 'w') as f:
                    f.write(commit_id + '\n')
        
                with open('commits.txt', 'r') as f:
                    commit_ids = f.read().splitlines()
                    for cid in commit_ids:
                        os.system(f'git cherry-pick {cid}')
                    os.system(' git add .')
                    os.system(f"git commit -m \"{commit_message_after_cherrypick}\"")
                    os.system("git push origin test")
    except Exception as e:
                logger.error(f"Something has happened in bring_changes_to_test function in test_sqrt.py file: {e}")
if __name__ == '__main__':
    bring_changes_to_test()
