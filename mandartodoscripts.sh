!#/bin/bash

git add *.py
git commit -m $1
git push origin master:remote
git status
