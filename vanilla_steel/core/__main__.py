import click
from vanilla_steel.core.task_organizer import TaskOrganizer, TaskOrganizerFactory
from vanilla_steel.core.plugin import PlugIn
from vanilla_steel.database.queries import insert_into_material_table
from vanilla_steel.database.models import Material
from vanilla_steel.config import logger
from rich.progress import Progress

def load_data(task: TaskOrganizer, source: str):
    logger.info(f"load data {source}")
    input_source: TaskOrganizer = task(source)
    records = [Material(**record) for _, record in input_source.formatted_records()]
    with Progress() as progress:
        task = progress.add_task("[cyan]Processing ...", total=len(records))
        for i, record in enumerate(records, 1):
            insert_into_material_table(record)
            progress.update(task, advance=1)
            progress.update(task, description=f"[cyan]Processing {i} out of {len(records)}")

@click.command(help="Load data into the application", epilog="A method to load data")
@click.option("--source", type=click.Choice(['1', '2', '3']), help="specify the source to load the data from")
def load(source):
    plugin = PlugIn()
    plugin.load("specifications.yaml")
    factory = TaskOrganizerFactory()
    source = f"InputSource{source}"
    factory.register(source, plugin.object[source].module)
    load_data(factory.funcs[source], plugin.object[source].metadata["source"])