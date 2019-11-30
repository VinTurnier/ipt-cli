import subprocess

from ipt_pk.scripts import configure

def api():
    config = configure.get_config()
    ipt_api_path = config['GIT REPOSITORIES']['ipt-api']
    print("Killing any ipt_local_db containers")
    subprocess.call("docker kill ipt_local_db",shell=True)
    print("Removing any ipt_local_db")
    subprocess.call("docker rm ipt_local_db",shell=True)
    print('starting api server: flask')
    subprocess.call(f'docker-compose -f {ipt_api_path}/docker-compose.yml up --build &',shell=True)

def database():
    config = configure.get_config()
    ipt_models_path = config['GIT REPOSITORIES']['ipt-models']
    print("Killing any ipt_local_db containers")
    subprocess.call("docker kill ipt_local_db",shell=True)
    print("Removing any ipt_local_db")
    subprocess.call("docker rm ipt_local_db",shell=True)
    print('starting database server: mysql')
    subprocess.call(f'docker-compose -f {ipt_models_path}/docker-compose.yml up --build &',shell=True)


def ngrok():
    subprocess.call("exec ngrok http 0.0.0.0:6000",shell=True)

def help():
    print("Usage: ipt start [OPTIONS]")
    print("Options:")
    print("  --api  To start flask api server")
    print("  --database  To start iptlocal database mysql instance")
    print("  --ngrok  To start the ngrok server")
    print("  --help  Show this message and exit.")