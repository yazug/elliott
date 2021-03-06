from __future__ import unicode_literals, print_function, with_statement
import click

from elliottlib import Runtime
from elliottlib.cli.common import cli, find_default_advisory
from elliottlib import errata

pass_runtime = click.make_pass_decorator(Runtime)


@cli.command('advisory-images', short_help='List of images in a given advisory')
@click.option(
    '--advisory', '-a', 'advisory',
    type=int, default=None, metavar='ADVISORY',
    help='Explicitly define image advisory ID to be used instead of the default')
@pass_runtime
def advisory_images_cli(runtime, advisory):
    """List images of a given advisory in the format we usually send to CCS (docs team)

    $ elliott advisory-images --advisory 48465

    If no `--advisory` is provided, elliott will use the default image advisory
    of the given group.

    $ elliott --group openshift-4.2 advisory-images
    """
    runtime.initialize(no_group=(advisory is not None))

    if advisory is None:
        advisory = find_default_advisory(runtime, 'image')

    print(errata.get_advisory_images(advisory))
