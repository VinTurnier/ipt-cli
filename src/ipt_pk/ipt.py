
# Standard Application Imports
import subprocess

# Third Party Imports
import click

from ipt_pk.scripts import initialize
from ipt_pk.scripts import configure as _configure
from ipt_pk.scripts import start as _start
from ipt_pk.scripts import stop as _stop

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
def configure(ipt_api,ipt_models):
    configuration = {
        'ipt-api':ipt_api,
    }
    _configure.read_config(configuration)


@cli.command()
def start():
    _start.api()

@cli.command()
def stop():
    _stop.api()

if __name__=='__main__':
    cli()