import subprocess
import datetime

from ipt_pk.scripts import configure

def production_database():
    config = configure.get_config()
    ipt_models_path = config['GIT REPOSITORIES']['ipt-models']
    print("Dumping into repo...")
    subprocess.call(f'cd {ipt_models_path}/test_db && ./get-production-db.sh',shell=True)
    print('Updating database container...')
    subprocess.call('docker exec  -it ipt_local_db /bin/bash ./update-db.sh',shell=True)

def help():
    print("Usage: ipt start [OPTIONS]")
    print("Options:")
    print("  --production-database  Dumps production database to local database")
    print("  --help  Show this message and exit.")