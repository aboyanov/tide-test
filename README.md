# Tide - Senior DevOps Engineer Test
Script that interact with a git tags

![](https://github.com/aboyanov/tide-test/blob/master/tide_logo.png)

Just for my own fun, I've completed the task using both: Python and Bash
> "It should have as few external dependencies as possible"

So the Bash script here is the winner

## Prerequisites:
* Git, Python3
```
sudo apt-get update \
sudo apt-get upgrade \
sudo apt-get install git python3
```

## Instructions for installing and running the script:
* Clone this repo and make the scripts executable:
```
git clone https://github.com/aboyanov/tide-test.git \
cd tide-test \
chmod +x test_py.py test_bash.sh
```

### Python
E.g.
```
git checkout -b my-feature
./test_py.py experiment
```
Would result in a set of tags like this:
```
my-feature
2019-01-09-14-24-22 (i.e. the current timestamp)
experiment
```

### Bash
./test_bash.sh
