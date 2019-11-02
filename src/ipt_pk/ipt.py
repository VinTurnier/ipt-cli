
# Standard Application Imports
import subprocess

# Third Party Imports
import click

from ipt_pk.scripts import initialize
from ipt_pk.scripts import configure as _configure
from ipt_pk.scripts import start as _start

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
        'ipt-models':ipt_models
    }
    _configure.read_config(configuration)


@cli.command()
def start_database():
    _start.database()

if __name__=='__main__':
    cli()