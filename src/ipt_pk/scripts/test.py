import subprocess
import datetime

from ipt_pk.scripts import configure

def database():
    config = configure.get_config()
    ipt_models_path = config['GIT REPOSITORIES']['ipt-models']
    print('Running test on database models...')
    print("Downloading ipt models local branch...")
    subprocess.call(f"pip install -e {ipt_models_path}",shell=True)
    print('updating database...')
    subprocess.call('docker exec  -it ipt_local_db /bin/bash ./update-db.sh',shell=True)
    print(f"Database up-to-date with production as of: {datetime.datetime.now()}\n")
    print("===========================================================================")
    print("                       Testing IPT Models                                  ")
    subprocess.call(f"python3 -m pytest {ipt_models_path}/src/ipt", shell=True)

def api():
    pass

def help():
    print("Usage: ipt start [OPTIONS]")
    print("Options:")
    print("  --database  To start iptlocal database mysql instance")
    print("  --help  Show this message and exit.")