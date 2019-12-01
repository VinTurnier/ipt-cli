IPT Command Line Interface
===

Welcome to the IPT Command Line Interface or ipt-cli repository. This CLI is used to help manage the ipt project. Due to the fact that there are many different repositories that are used in this project the goal of ipt-cli is to use the command line interface to run test, upgrades, containers, manage aws, etc... By having the CLI you now spend less time figuring out where a script or directory is located, and more time runing your code.

# Pre-requisites
- the ipt-cli uses `docker` to run local servers and databases, please make sure you have that installed before using the CLI
- Add the `.my.cnf` file to the `ipt-models/test_db` directory so that the docker can have access to it. Also create a similar file in your home directory with the same credentials.
- mysql installed `brew install mysql`
- pipe viewer installed `$ brew install pv`

# Installation
To install this command line interface simply use the python package manager `pip`:
```s
$ pip install git+https://git@github.com/vinturnier/ipt-cli.git@master#egg=ipt_pk
```
This command will download the latest version of the cli. Once you have ran this command in your terminal you can now use the ipt-cli. To know if it was installed successfully run `ipt` in your terminal.

NOTE: sometimes you also have to add the python path to the CLI to your `$PATH` environment varaible. so that it is possible to run it from anywhere in your terminal. If you have to add a new path to `$PATH`, it might be necessary to restart your terminal window.

# Configuration
Once you have it installed you are now ready to configure the ipt-cli. First step is to run the `init` command:
```s
$ ipt init
```
After doing so run the configure command:
```s
$ ipt configure
```
This will prompt you to enter the location of the `ipt-models` and `ipt-api` directory (They are repos that you clone locally) for me it looks like this:
```s
$ Enter ipt-api repository path: ~/ipt-project/ipt-api
$ Enter ipt-models repository path: ~/ipt-project/ipt-models
```
Make sure <b>TO NOT ADD</b> the forward slash at after `ipt-models` or `ipt-cli`. You are now ready to use the ipt commands.

# Using the Commands

Lets first start with an easy command that should not ask for any configuration of the other repositories. The first command we will run is to start the local database container for the ipt project.
```s
$ ipt start --database
```
This commands spins up a mysql:8.0.11 database container on your local machine. This mysql instance will most likely have data in there already to use. If there is None, you can use the ipt dump command to update the database.
```s
$ ipt dump --production-database
```
Simply start the container again and your will now have production data on your local environment. This guarantees that your local database will always be similar to your production database. 
