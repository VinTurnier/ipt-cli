# ipt-cli
Command Line Interface for ipt project

# To Start
Download all the necessary repos onto your local machine:
- ipt-api
- ipt-models
Once downloaded you will install the cli on your local machine. To do this you first need to make sure you have [ssh-keygen](https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) for github, so that you can `pip install` from private repos. Once you have your key setup you should now be able to install the ipt-cli by running the following command:
```s
pip install -e git+ssh://git@github.com/username/ipt-cli.git@master#egg=ipt
```
Now make sure to change the username to your username, and change master to the version that you would like the use. The latest version is `0.3.6-beta`. Once you have that installed on your local machine, we will setup the other repos that you downloaded. 

## Setting up ipt-api
To setup `ipt-api` you must first add a file called `web.env` to the root of the folder. This will contain your twilio keys.
```s
# ipt-api/web.env
Twilio_Account_SID='account sid'
Twilio_Auth_Token='auth token'
```
This file is important as docker relies on it to connect to twilio. Once that is setup all you have to do it run the following commands:
- first:
```s
$ ipt init
```
- second
```s
$ ipt configure
```