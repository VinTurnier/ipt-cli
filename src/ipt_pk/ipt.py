
# Standard Application Imports
import subprocess

# Third Party Imports
import click

from ipt_pk.scripts import initialize
from ipt_pk.scripts import configure as _configure
from ipt_pk.scripts import start as _start
from ipt_pk.scripts import stop as _stop
from ipt_pk.scripts import test as _test

@click.group()
def cli():
    pass

@cli.command()
def init():
    initialize.create_ipt_config_directory()

@cli.command()
def install_packages():
    initialize.install_requirements()

@cli.command()
@click.option('--ipt_api',prompt='Enter ipt-api repository path')
@click.option('--ipt_models',prompt='Enter ipt-models repository path')
def configure(ipt_api,ipt_models):
    configuration = {
        'ipt-api':ipt_api,
        'ipt-models': ipt_models
    }
    _configure.read_config(configuration)


@cli.command()
@click.option('--api','switch',flag_value='api')
@click.option('--database','switch',flag_value='database')
@click.option('--ngrok','switch',flag_value='ngrok')
def start(switch):
    if(switch=='api'):
        _start.api()
    elif(switch=='database'):
        _start.database()
    elif(switch=='ngrok'):
        _start.ngrok()
    else:
        _start.help()


@cli.command()
@click.option('--api','switch',flag_value='api')
@click.option('--database','switch',flag_value='database')
def stop(switch):
    if(switch=='api'):
        _stop.api()
    elif(switch=='database'):
        _stop.database()
    elif(switch=='all'):
        _stop.all()
    else:
        _stop.help()


@cli.command()
@click.option('--api','switch',flag_value='api')
@click.option('--database','switch',flag_value='database')
def test(switch):
    if(switch=='api'):
        _test.api()
    elif(switch=='database'):
        _test.database()
    else:
        _test.help()


if __name__=='__main__':
    cli()
