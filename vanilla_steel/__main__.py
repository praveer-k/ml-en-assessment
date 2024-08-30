from vanilla_steel.core.task_organizer import TaskOrganizer, TaskOrganizerFactory
from vanilla_steel.core.plugin import PlugIn
from vanilla_steel.database.queries import insert_into_material_table
from vanilla_steel.database.models import Material
from vanilla_steel.llm.categorizer import Categorizer
from vanilla_steel.config import logger, settings
from vanilla_steel.config.logger import LogLevel
from vanilla_steel.docs.__main__ import DocumentationBuilder
from tqdm import tqdm
import os
import click
import subprocess

def load_data(task: TaskOrganizer, source: str):
    logger.info(f"load data {source}")
    input_source: TaskOrganizer = task(source)
    records = [Material(**record) for _, record in input_source.formatted_records()]
    for record in tqdm(records):
        print(record)
    #     insert_into_material_table(record)

@click.command(help="Load data into the application", epilog="A method to load data")
@click.option("--source", type=click.Choice(['1', '2', '3']), help="specify the source to load the data from")
def load(source):
    plugin = PlugIn()
    plugin.load("specifications.yaml")
    factory = TaskOrganizerFactory()
    source = f"InputSource{source}"
    factory.register(source, plugin.object[source].module)
    load_data(factory.funcs[source], plugin.object[source].metadata["source"])

@click.command(help="Categorize data using LLM", epilog="A method to categorize data")
def categorize():
    Categorizer().run()
   
@click.command(help="Show Dashboard", epilog="A method to show dashboard")
def dashboard():
    logger.info("show dashboard")
    subprocess.run(["streamlit", "run", "./vanilla_steel/dashboard/__main__.py"])

@click.command(help="Build, Watch or Serve Docs", epilog="A method to build, serve documentation")
@click.option("--build", is_flag=True, help="Build Sphinx docs")
@click.option("--watch", is_flag=True, help="Watch for changes in document source directory")
@click.option("--serve", is_flag=True, help="Start the document server")
def docs(build, watch, serve):
    logger.info("show documentations")
    SCR_DIR = os.path.abspath(settings.DOCS.SOURCE_DIR)
    BLD_DIR = os.path.abspath(settings.DOCS.BUILD_DIR)
    CACHE_DIR = os.path.abspath(settings.DOCS.CACHE_DIR)
    logger.warning(f"Source dir: {SCR_DIR}")
    logger.warning(f"Build dir: {BLD_DIR}")
    logger.warning(f"Cache dir: {CACHE_DIR}")
    doc = DocumentationBuilder(src_dir=SCR_DIR, build_dir=BLD_DIR, cache_dir=CACHE_DIR)
    doc.download_dependencies()
    if build:
        doc.build()
    elif watch:
        doc.build().watch()
    elif serve:
        doc.build().serve()

@click.group()
@click.option("--debug", is_flag=True, default=False, help="Enable debug mode")
def main(debug):
    settings.LOG_LEVEL = LogLevel.DEBUG if debug==True else settings.LOG_LEVEL
    logger.warning(f"Debug mode is {'on' if debug else 'off'}")

main.add_command(load)
main.add_command(categorize)
main.add_command(dashboard)
main.add_command(docs)
    
if __name__ == "__main__":
    main()

