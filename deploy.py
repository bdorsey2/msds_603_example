import paramiko
from os.path import expanduser 
from user_definition import *

ssh = paramiko.SSHClient()
print(ssh)

ec2_address = "ec2-54-149-49-78.us-west-2.compute.amazonaws.com"
user = "ec2-user"
key_file = "briand.pem"

ssh.connect(ec2_address, username = user, key_filename = expanduser("~") + key_file)

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
ssh.connect(ec2_address, username = user, key_filename = expanduser("~") + key_file)

stdin, stdout, stderr = ssh.exec_command("conda env create -f ~/msds603_instructor/environment.yml")
#print(stderr.read())
if(b'already exists' in stderr.read()):
    stdin, stdout, stderr = ssh.exec_command("conda env update -f ~/msds603_instructor/environment.yml")
    #print(stderr.read())
    #print(stdout.read())

stdin, stdout, stderr = ssh.exec_command("git --version")

print(stdout.read())
print(stderr.read())

git_repo_owner = "MSDS698"
git_repo_name = "2019-msds603-example"
git_user_id = "dianewoodbridge"

if (b"" is stderr.read()):
    git_clone_command = "git clone https://github.com/" + git_user_id + "/" + git_repo_name + ".git"
    #git_clone_command = "git clone https://" + git_user_id + "@github.com/" + git_repo_owner + "/" + git_repo_name + ".git"
    stdin, stdout, stderr = ssh.exec_command(git_clone_command)
    print(stdout.read())
    print(stderr.read())

## TODO HANDLE ALREADY EXISTS EXCEPTION