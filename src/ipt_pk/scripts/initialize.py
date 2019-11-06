import subprocess
import os
import sys
import time

from ipt_pk.scripts import configure

def create_ipt_config_directory():
    path = '~/.ipt'
    status = subprocess.call("cd {}".format(path), shell=True)

    if status == 1:
        print('creating ~/.ipt directory...')
        time.sleep(1)
        subprocess.call('mkdir -p ~/.ipt && touch ~/.ipt/config.ini',shell=True)
    else:
        print('-------------------------------------------')
        print('------------- IPT CLI ---------------------')
        print('~/.ipt already exist...')
        print('-------------------------------------------')
        print('')
        print('Configure .ipt/config.ini file')
        print('')
        print('-------------------------------------------')
        print('run the following command to configure ipt:')
        print('$ ipt configure')
        print('-------------------------------------------')

        return True

def install_requirements():
    if hasattr(sys,'real_prefix') == False:
        print('--------------------------------------------------')
        print('-------------------- IPT CLI ---------------------')
        print('--------------------------------------------------')
        print('Start virtualenv by running the following command:')
        print('source venv/bin/activate')
        print('--------------------------------------------------')
        return False

    config = configure.get_config()
    ipt_api_path = config['GIT REPOSITORIES']['ipt-api']

    print('installing all required packages for ipt-api')
    subprocess.call(f'pip install -r {ipt_api_path}/requirements.txt',shell=True)
    print('All Packages are installed')



