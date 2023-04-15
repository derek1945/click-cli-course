# greeter.py

import click


@click.command()
@click.argument('first_name')
@click.argument('last_name')
@click.option('--lang',
              help='Specify language English (en) or Polish (pl)',
              default='en',
              type=click.Choice(['en', 'pl']))
def greet(first_name, last_name, lang):
    """Displays a greeting to the user."""
    if lang == 'en':
        greetings = 'Hello'
    elif lang == 'pl':
        greetings = 'Czesc'
    else:
        raise click.BadOptionUsage('lang', 'Unsupported language.')
    click.echo(f"{greetings} {first_name} {last_name}")
    