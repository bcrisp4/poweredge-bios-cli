'''
Dell PowerEdge BIOS CLI
'''
import json
import click
from poweredge_bios_cli.client import Client


@click.group()
@click.option('-h', '--host', prompt=True, required=True,
              help='The hostname or IP of the server iDRAC interface.')
@click.option('-u', '--username', prompt=True, required=True,
              help='The iDRAC username to use for authentication.')
@click.option('-p', '--password', prompt=True, hide_input=True, required=True,
              help='The password for the specified iDRAC user.')
@click.option('--verify-ssl', 'ssl_verify', default=True, type=bool,
              help='Verify SSL/TLS certificates. Defaults to \'true\'.')
@click.pass_context
def cli(ctx, username, password, host, ssl_verify):
    '''
    A command-line interface for the Dell PowerEdge server BIOS using
    the RedFish API.

    NOTE: RedFish must be enabled on the server iDRAC for this to work
    and the user you specify must have the relevant permissions granted
    to interact with the BIOS via the API.

    The options --host, --username and --password are required.
    If these options are not specified, you will be prompted to
    provide values for these options interactively.

    For more information on the Dell implementation of RedFish on
    PowerEdge servers, see https://dell.to/30gB3Fu \
    '''
    ctx.obj = Client(username, password, host, ssl_verify)


@cli.command()
@click.pass_obj
@click.argument('attributes', nargs=-1)
def get(client, attributes):
    '''
    Get the specified attributes or all attributes if 'all' is specified.
    '''
    bios_attributes = client.get_bios_attributes(attributes)
    if bios_attributes:
        output = json.dumps(bios_attributes, indent=2)
        click.echo(output)
