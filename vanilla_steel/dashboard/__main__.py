import click
import subprocess
from vanilla_steel.config import logger

@click.command(help="Show Dashboard", epilog="A method to show dashboard")
def dashboard():
    logger.info("show dashboard")
    subprocess.run(["streamlit", "run", "./vanilla_steel/dashboard/page.py"])

