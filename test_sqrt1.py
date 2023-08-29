import os, pytest, logging, subprocess, json
from dotenv import load_dotenv
from sqrt import *
# Load environment variables
load_dotenv()

# Declare global variables
owner = 'nksharma063'
repo = 'CICD_Project'
token = os.environ['GIT_TOKEN']
auth_token = os.environ['GIT_AUTH_TOKEN']

# Define test scripts
def test_hello():
    a = hello()
    assert a == "hi breakout 4"

def test_registration():
    a = registration()
    assert a == "Welcome to registration room"

def update_status():
    # Set the status information
    state = 'success'
    context = 'continuous-integration/jenkins'
    description = 'The build succeeded!'

    # Check if the commits.txt file exists
    if os.path.exists('commits.txt'):
        print("Success")    
        with open('commits.txt', 'r') as f:
            # Read the commit IDs from the file
            commit_ids = f.read().splitlines()
            print(commit_ids, type(commit_ids))
            for commit_id in commit_ids:
                # POST the commit status to "Success"
                status = subprocess.check_output(['curl', '-X', 'POST', '-H', f'Authorization: Bearer {auth_token}', '-H', 'Content-Type: application/json', '-d', f'{{"state":"{state}", "context":"{context}", "description":"{description}"}}', f'https://api.github.com/repos/{owner}/{repo}/statuses/{commit_id}'])
                status = json.loads(status.decode('utf-8'))
                print(status)
    else:
        print("Commit txt File not found")

def git_commit_and_push(file_path, commit_message, branch):
    os.system(f"git add {file_path}")
    os.system(f"git commit -m '{commit_message}'")
    os.system(f"git push origin {branch}")

if __name__ == "__main__":
    # Run the tests and check if they passed
    exit_code = pytest.main()
    test_passed = (exit_code == 0)
    if test_passed:
        update_status()
        os.system("git stash")
        os.system("git checkout test -f")
        dir = 'D:\\DevOps_HerVired\\CICD\\CICD_Project'
        file = os.path.join(dir, 'commits.txt').replace('\\', '/')
        commit_message = 'Add: commits.txt file'
        git_commit_and_push(file, commit_message, 'test')
        print("File uploaded to remote successfully")
    else:
        logging.error("Please check the test cases or fix the bug")

