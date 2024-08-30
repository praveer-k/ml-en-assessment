import click
from .categorizer import Categorizer

@click.command(help="Categorize data using LLM", epilog="A method to categorize data")
def categorize():
    Categorizer().run()