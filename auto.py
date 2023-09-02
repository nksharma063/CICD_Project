import json
import subprocess
import os
from dotenv import load_dotenv
import logging

load_dotenv()
token = os.environ['GIT_TOKEN']

logging.basicConfig(filename="record.log", level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadname)s : %(message)s')

def pull_file_commits(file, dir):
    try:
        # os.system('git stash')
        file_path = file_path = os.path.join(dir, file).replace('\\', '/')
        os.system('git checkout dep')
        os.system(f'git checkout test -- {file}')
        print("++++++----", file_path)
        return file_path
    except:
        logger.error("Unable to pul the commits file from test branch, please ask on Slack or Teams or check what happened while ulling the files")

def status_check():
    file_path = pull_file_commits('commits.txt', 'D:\\DevOps_HerVired\\CICD\\CICD_Project')
    try:
        if os.path.exists(file_path) and os.path.isfile('commits.txt'):  
            with open(file_path, 'r') as f:
                commitID =  f.read().splitlines()
                print("+++++++", commitID)
                #    for each in commitIDs:
                #        commitID = each
            commitID = commitID[0]
            print(")))))((((((((()))))))))", commitID)
            commit_status = subprocess.check_output(['curl', '-L'  , '-H' ,'Accept: application/vnd.github+json',   '-H', 'token',   '-H', 'X-GitHub-Api-Version: 2022-11-28',   f'https://api.github.com/repos/nksharma063/CICD_Project/commits/{commitID}/status'])
            commit_status = json.loads(commit_status.decode('utf-8'))
            print(commit_status['state'])
            commit_status = commit_status['state']
    except:
        logger.error("Please check the error with the request or filepath which not reading teh COMMITID as status is not fetched")
    return commit_status


if __name__ == '__main__':
    pull_file_commits('commits.txt', 'D:\\DevOps_HerVired\\CICD\\CICD_Project')
    state = status_check()
    print(state)
    try:
        if state == 'success':
            # os.system(lsof :80  localhost | kill)
            os.system("git checkout dev -- sqrt.py")
            # os.system("pip install requirements.txt")
        

            # os.syste()
        else:
            logger.error("Pata karo kya hua main fucntion mai, This could be because state is not correct or pull file commits are not working")
            






# commits = subprocess.check_output(['curl', '-L'  , '-H' ,'Accept: application/vnd.github+json',   '-H', 'token',   '-H', 'X-GitHub-Api-Version: 2022-11-28',   'https://api.github.com/repos/nksharma063/CICD_Project/commits/REF/status'])

# commits = json.loads(commits.decode('utf-8'))
# COMMITID = commits[0]['sha']
# commit_message = commits[0]['commit']['message']
# print(COMMITID, commit_message)





"""
Rough Work
# import requests, os

# def check_for_new_commits():
#     headers = {'Authorization': f'token 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'}
#     url = f'https://api.github.com/repos/TeamKanyarasi/CICD_Project/commits?sha=prod'
#     response = requests.get(url, headers=headers)
#     commit_ids = []
#     latest_commit_id = None

#     if response.status_code == 200:
#         commits = response.json()
#         print(f'New commits found: {len(commits)}')
#         for commit in commits:
#             commit_ids.append({commit["sha"]})
#         print(commit_ids)
#     else:
#         print(f'Error: {response.status_code}')
    
#     if commit_ids[0] != latest_commit_id:
#         latest_commit_id = commit_ids[0]
#         # print(latest_commit_id)
#         os.system('git pull origin prod')
#         os.system('sudo cp -rf *.html /var/www/html/')
#         os.system("sudo service nginx restart")


# check_for_new_commits()
"""
