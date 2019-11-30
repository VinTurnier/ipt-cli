import subprocess

from ipt_pk.scripts import configure

def api():
    config = configure.get_config()
    ipt_api_path = config['GIT REPOSITORIES']['ipt-api']
    print('Stopping api server: flask')
    subprocess.call(f'docker-compose -f {ipt_api_path}/docker-compose.yml stop',shell=True)

def database():
    config = configure.get_config()
    ipt_model_path = config['GIT REPOSITORIES']['ipt-models']
    print('Stopping database server: mysql')
    subprocess.call(f'docker-compose -f {ipt_model_path}/docker-compose.yml stop',shell=True)

def help():
    print("Usage: ipt stop [OPTIONS]")
    print("Options:")
    print("  --api  to start flask api server")
    print("  --database  to start iptlocal database mysql instance")
    print("  --help  Show this message and exit.")
