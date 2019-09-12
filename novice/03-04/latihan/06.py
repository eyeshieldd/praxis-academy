import click

from flask import Flask

app = Flask(__name__)

@app.cli.command('hello')
@click.option('--name', default='World')
def hello_command(name):
    click.echo(f'Hello, {name}')

def test_hello():
    runner = app.test_cli_runner()

    result = runner.invoke(hello_command, ['--name', 'Flask'])
    assert 'Hello, Flask' in result.output

    result = runner.invoke(args=['hello'])
    assert 'World' in result.output