import subprocess

from ipt_pk.scripts import configure

def database():
    config = configure.get_config()
    ipt_models_path = config['GIT REPOSITORIES']['ipt-models']
    
    print('Killing ipt_local_db before starting database...')
    subprocess.call('docker kill ipt_local_db',shell=True)
    print('starting database: ipt_local_db')
    subprocess.call(f'docker-compose -f {ipt_models_path}docker_db/docker-compose.yml up --build &',shell=True)

def api(ctx,param,value):
    config = configure.get_config()
    ipt_api_path = config['GIT REPOSITORIES']['ipt-api']
    
    print('starting api server: flask')
    subprocess.call(f'python {ipt_api_path}api.py',shell=True)