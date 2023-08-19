import pytest, requests
import os, logging


exit_code = pytest.main(["-x", "test_sqrt.py"])
result = (exit_code == 0)
print(result)





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