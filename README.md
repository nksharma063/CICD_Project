#### In order to work this project

Please clone the repo.
Create one PAT fine grained token.
Copy paste the curl command.
Create one .json file and read teh file to copy paste into the curl command. i used .env file os.environ methods to read it.

Cron Job need to run on bash script every 30 minutes to copy paste the .html code to nginx server and auto.py file to check the status and bring the file or changes in the file.
 

# CICD_Project
## Dev Branch

## sqrt.py /abc.html
   a) This file will is core development file on which rigourous neural network is working.
   b) all changes will be done in these file to check the commits further
   c) Developer will keep working on these file and deliver the print fucntion sin flask through dev branch without any subbranch.

## Test Branch
### test_sqrt.py
  a) This file will check the commit ID and commit message with commit ID.
  b) #### commit_comment(commit_id) : 
      This fucntion will pull the commnets o the commit ID
  c) This will use github API and curl request to bring details of git.

#### Till now we have comment on commit and message from developer to process further
  a) We will bring the changes happened in development file to the test branch using commit_id, first_word_of_commit_message, first_word_of_comment
  b) We will and create one commits.txt file to store the recent commit.

### test_sqrt1.py
  a) We will write and run basic test cases using PYTEST lib based on changes reflected in the dev file.
  b) We wcan create and test cases first or integrate in the the file as well. I recomment to create the test cases and execute them in individual file first to test everything.
  c) We will use  update_status() to read the commit ID and then check the status, if status is success
  d) We will push the "commits.txt" file to remote test.

## Dep Branch

### Auto.py file

  a) We will first fetch the file path after the pulling the commits.txt file
  b) we will read the file fr the commit_ID and check for status
  c) if status is sucess updated by test team then it will pull the dev file to the dep branch and working dircetory to track changes.

### deploy.sh
a) This file first stope the nginx code using service or systemctl f enabled.
b) It will copy paste the .html file to /var/www/html/
c) restart the nginx

 
  
