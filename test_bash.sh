#!/bin/bash

timestamp=$(date "+%Y-%m-%d-%H-%M-%S")
git tag $timestamp

curr_branch=$(git rev-parse --abbrev-ref HEAD)
if [ $curr_branch != "master" ]; then
    git tag $curr_branch
fi

if [ $# -eq 1 ]; then
    git tag $1
fi

#git push origin --tags
