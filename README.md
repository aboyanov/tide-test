# Tide - Senior DevOps Engineer Test

![](https://github.com/aboyanov/tide-test/blob/master/tide_logo.png)

## The task:
```
Using the language of your choice, write a script that when run from inside a git repository:
  ● Will create a git tag containing the current time and date.
  ● If the current branch is not master will create another git tag containing the name of the current branch.
  ● If supplied with an optional parameter will also create a git tag containing the value of that parameter.
  ● Will push all created tags to `origin`.
```

------------
Just for my own fun, I've completed the task using both: Python and Bash
> "It should have as few external dependencies as possible"

So the **Bash** script here is the winner

------------

## Prerequisites:
* Install: git and python3

  E.g.: Debian/Ubuntu Linux based system
```
sudo apt-get update; \
sudo apt-get upgrade; \
sudo apt-get install git python3
```

## Instructions for installing and running the scripts:
* Clone this repo and make the scripts executable:
```
cd ~; \
git clone https://github.com/aboyanov/tide-test.git; \
cd ./tide-test; \
chmod u+x test_py.py test_bash.sh
```
### Bash
Example usage:
```
git checkout -b my-feature
./test_bash.sh experiment
```
You will be prompted to provide your git credentials next, in order for the script to push the created tags to `origin`.
Note: if you follow the steps, it will try to push to this repo :)
If you want to use it in your repo, move the script /to/your/git/repo
```
mv ./test_bash.sh /path/to/your/git/repo
```
And then execute it, the same way like before:
```
./test_bash.sh optional-arg
```

Would result in a set of tags like this:
```
my-feature
2019-01-09-14-24-22 (i.e. the current timestamp)
experiment
```
### Python
The same applies for the python script like for the bash
Example usage:
```
git checkout master
./test_py.py experiment
```
Would result in a set of tags like this, because when you are on the master branch, it won't create a tag with the current branch name:
```
2019-01-09-14-24-22 (i.e. the current timestamp)
experiment
```
See the created tags:
```
git tag
```
