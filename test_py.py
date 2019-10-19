#!/usr/bin/python3
import sys
from datetime import datetime
import subprocess

def git_tag(tag):
    subprocess.call(["git", "tag", tag])

def main(args):
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    git_tag(timestamp)
   
    # get current branch name
    command = "git symbolic-ref --short -q HEAD"
    curr_branch = subprocess.Popen(command,
            shell=True, 
            stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
    
    if curr_branch != 'master':
        git_tag(curr_branch)
    
    if len(args) > 1:
        git_tag(args[1])
    
    # push tags to origin
    subprocess.call(["git", "push", "origin", "--tags"])

if __name__ == '__main__':
    main(sys.argv)
