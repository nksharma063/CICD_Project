import pytest, requests
import os, logging
# from dotenv import load_dotenv
# def main():
#     exit_code = exit_code()
#     if exit_code == 'Success':

def exit_code_test():
    # os.chdir("D:\DevOps_HerVired\CICD\CICD_Project")
    # os.system("git checkout dep")
    # os.system("git pull origin/dev sqrt.py")
    # os.system("git pull origin/test test_sqrt.py")
    # os.system("sudo chmod +x sqrt.py")
    # os.system("sudo chmod +x test_sqrt.py")
    # os.system("chmod +x sqrt.py")
    exit_code = pytest.main(["-x", "test_sqrt.py"])
    result = (exit_code == 0)
    print(result)
    # if result == True:
        # print(")

        # os.system("git add sqrt.py")
        # os.system("git commit -m "Updating: Pushing the file to dep branch")
        # os.system("git push ")                  
        # print(result)
        # if result == ""
#     else:
#         logging.ERROR("Please check some test has failed")
#         return "Failure"
exit_code_test()
# def check_for_new_commits():
#     # Set variables
#     owner = "nksharma063"
#     repo = "CICD_Project"
#     branch = "dep"
#     access_token = 
#     latest_commit_id_file = f'https://api.github.com/repos/{owner}/{repo}/commits?sha={branch}/latest_commit_id_file.txt'

#     # Read latest commit ID from file
#     try:
#         with open(latest_commit_id_file, "r") as f:
#             latest_commit_id = f.read().strip()
#     except: 
#         logging.critical (f"file is not available")
#         latest_commit_id = None

#     # Check for new commits
#     headers = {'Authorization': f'token {access_token}'}
#     url = f'https://api.github.com/repos/{owner}/{repo}/commits?sha={branch}'
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         commits = response.json()
#         print(f'New commits found: {len(commits)}')
#         if commits[0]["sha"] != latest_commit_id:
#             # Update latest commit ID
#             with open(latest_commit_id_file, "w") as f:
#                 f.write(commits[0]["sha"])

#             # Change to the directory containing the repository
#             os.chdir('D:\DevOps_HerVired\flask_project\flask_project')

#             # Pull the latest code
#             os.system('git checkout dep')
#             os.system('git pull origin dep')

#             # Copy flask files to web server directory
#             os.system('sudo cp -rf *.html *.py /var/www/html/')

#             # Restart Nginx
#             os.system("sudo service nginx restart")
#     else:
#         logging.ERROR(f'Error: {response.status_code}')





# # github username
# username = "x4nth055"
# # url to request
# url = f"https://api.github.com/users/{username}"
# # make the request and return the json
# user_data = requests.get(url).json()
# # pretty print JSON data
# pprint(user_data
# https://docs.gitlab.com/ee/api/commits.html

# You  to  Everyone 11:59
# https://docs.github.com/en/rest/commits/statuses?apiVersion=2022-11-28

# Himani Singh  to  Everyone 12:24
# https://github.com/himani0550/CICDpipeline-HTML/tree/dev

# Himani Singh  to  Everyone 12:29
# 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

# charan Yandrapu  to  Everyone 12:31
# from github import Github
# import time

# # First create a Github instance:
# # using an access token
# g = Github("<access_token>")

# # Then play with your Github objects:
# repo = g.get_repo("<owner>/<repo>")
# last_commit_sha = None

# while True:
#     commits = repo.get_commits()
#     latest_commit = commits[0]
#     if last_commit_sha != latest_commit.sha:
#         print(f"New commit: {latest_commit.sha}")
#         last_commit_sha = latest_commit.sha
#     time.sleep(60)

# You  to  Everyone 12:44
# while true; do
#     git fetch origin
#     NEW_COMMITS=$(git log origin/prod..origin/dev --oneline)
#     if [ -n "$NEW_COMMITS" ]; then
#         echo "New commits found on dev branch that are not on prod branch:"
#         echo "$NEW_COMMITS"
#     else
#         echo "No new commits found on dev branch that are not on prod branch"
#     fi
#     sleep 300 # wait for 5 minutes before checking again
# done

# You 12:49
# curl -L \
#   -H "Accept: application/vnd.github+json" \
#   -H "Authorization: Bearer <YOUR-TOKEN>" \
#   -H "X-GitHub-Api-Version: 2022-11-28" \
#   https://api.github.com/repos/OWNER/REPO/commits/REF/status