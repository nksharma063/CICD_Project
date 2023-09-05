import json
import subprocess
import os
from dotenv import load_dotenv
from flask import logging

load_dotenv()
token = os.environ['GIT_TOKEN']

logging.basicConfig(filename="record_auto.log", level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadname)s : %(message)s')

def pull_file_commits(file, dir):
    try:
        # os.system('git stash')
        file_path = file_path = os.path.join(dir, file)#.replace('\\', '/') for windows section ony
        os.system('git checkout dep')
        os.system(f'git checkout test -- {file}')
        print("++++++----", file_path)
        return file_path
    except:
        logger.error("Unable to pul the commits file from test branch, pleae check the pull fle commit fucntion in auto.py file")

def pull_devbranch_file_and_changes_to_depbranch_filepath(file, dir):
    try:
        # os.system('git stash')
        file_path = file_path = os.path.join(dir, file)#.replace('\\', '/') for windows section ony
        os.system('git checkout dep')
        os.system(f'git checkout dev -- {file}')
        print("++++++----", file_path)
        return file_path
    except:
        logger.error("Unable to pul the commits file from test branch, pleae check the pull fle commit fucntion in auto.py file")

def status_check():
    file_path = pull_file_commits('commits.txt', '/mnt/d/DevOps_HerVired/CICD/CICD_Project')
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
        logger.error("Please check the error with the request or filepath which not reading teh COMMITID as status is not fetched, please check the status check fucntion in auto.py file")
    return commit_status


if __name__ == '__main__':
    pull_file_commits('commits.txt', '/mnt/d/DevOps_HerVired/CICD/CICD_Project/')    
    state = status_check()
    print(state)
    try:
        if state == 'success':
            if os.path.exists('app.py'):
                if os.path.exists('commits.txt'):
                    with open('commits.txt', 'r') as f:
                        commit_ids = f.read().splitlines()
                        for cid in commit_ids:
                            os.system(f'git cherry-pick {cid}')
            else:
                pull_devbranch_file_and_changes_to_depbranch_filepath('app.py', '/mnt/d/DevOps_HerVired/CICD/CICD_Project/')
                if os.path.exists('app.py'):
                    if os.path.exists('commits.txt'):
                        with open('commits.txt', 'r') as f:
                            commit_ids = f.read().splitlines()
                            for cid in commit_ids:
                                os.system(f'git cherry-pick {cid}')
    except Exception as e:
                logger.error(f"Something has happened in pull_devbranch_file_and_changes_to_depbranch_filepath or pull_file_commits function in auto.py file in dep branch: {e}")

            # os.system(lsof :80  localhost | kill)
            # os.system("git checkout dev -- app.py")
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
#     headers = {'Authorization': f'token AQdfQVY1wap85NqUtj4oUAGMU2YYT2HJI4A0OQN'}
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
