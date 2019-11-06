import subprocess

from ipt_pk.scripts import configure

def api():
    config = configure.get_config()
    ipt_api_path = config['GIT REPOSITORIES']['ipt-api']
    print('Stopping api server: flask')
    subprocess.call(f'docker-compose -f {ipt_api_path}/docker-compose.yml stop',shell=True)