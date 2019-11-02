import configparser

import os

def get_config():
    config = configparser.ConfigParser()
    user_path = os.path.expanduser('~')
    config.read(f'{user_path}/.ipt/config.ini')
    return config

def configure_git_repositories(config,data):
    config['GIT REPOSITORIES'] = data 
    user_path = os.path.expanduser('~')
    with open(f'{user_path}/.ipt/config.ini','w') as configfile:
        config.write(configfile)


def read_config(new_data):
    config = configparser.ConfigParser()
    user_path = os.path.expanduser('~')
    config_file = config.read(f'{user_path}/.ipt/config.ini')
    if config_file == []:
        print('----------------------------------')
        print('Initialize ipt before configuring:')
        print('$ ipt init')
        print('----------------------------------')
        return False

    configure_git_repositories(config,new_data)
    print('git repository path added to config.ini')
