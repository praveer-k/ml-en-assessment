import click
from vanilla_steel.config import logger, settings
from vanilla_steel.config.logger import LogLevel
from vanilla_steel.docs.__main__ import docs
from vanilla_steel.dashboard.__main__ import dashboard
from vanilla_steel.core.__main__ import load
from vanilla_steel.llm.__main__ import categorize
from vanilla_steel.version import show_version

@click.group()
@click.option("--debug", is_flag=True, default=False, help="Enable debug mode")
def main(debug):
    settings.LOG_LEVEL = LogLevel.DEBUG if debug==True else settings.LOG_LEVEL
    logger.warning(f"Debug mode is {'on' if debug else 'off'}")

if __name__ == "__main__":
    main.add_command(load)
    main.add_command(categorize)
    main.add_command(dashboard)
    main.add_command(docs)
    main.add_command(show_version)
    main()

