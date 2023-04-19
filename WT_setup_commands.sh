# the git commands can't be run since... you have to git pull the repo to access this file.
# a solution could be to mount this set up file from the server filesystem for immediate access in the tail
# for now, use this and WT_setup_instructions.txt as guide/docs!
git init
git remote add origin https://github.com/htmdec/ucsb
git pull
git checkout master
pip install -r requirements.txt

