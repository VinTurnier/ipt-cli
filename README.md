# ipt-cli
Command Line Interface for ipt project

# To Start
Download all the necessary repos onto your local machine:
- ipt-api
- ipt-models
Once downloaded you will install the cli on your local machine. To do this you first need to make sure you have [ssh-keygen](https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) for github, so that you can `pip install` from private repos. Once you have your key setup you should now be able to install the ipt-cli by running the following command:
```s
pip install -e git+ssh://git@github.com/username/ipt-cli.git@
```
