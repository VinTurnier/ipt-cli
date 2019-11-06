import subprocess

from ipt_pk.scripts import configure

def api():
    config = configure.get_config()
    ipt_api_path = config['GIT REPOSITORIES']['ipt-api']
    print('starting api server: flask')
    subprocess.call(f'docker-compose -f {ipt_api_path}/docker-compose.yml up --build &',shell=True)

def ngrok():
    subprocess.call("exec ngrok http 0.0.0.0:6000",shell=True)