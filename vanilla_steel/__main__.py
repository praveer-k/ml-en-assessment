from vanilla_steel.task_organizer.task_organizer import TaskOrganizer
from vanilla_steel.task_organizer.input_source_1 import InputSource1
from vanilla_steel.task_organizer.input_source_2 import InputSource2
from vanilla_steel.task_organizer.input_source_3 import InputSource3
from vanilla_steel.database.queries import insert_into_material_table
from vanilla_steel.database.models import Material
from vanilla_steel.config import logger
from pydantic.dataclasses import dataclass
from typing import Optional, Literal
from tqdm import tqdm
import argparse

class ArgumentError(Exception):
    def __init__(self, message):            
        super().__init__(message)

def load_data(task: TaskOrganizer, source: str):
    logger.info(f"load data {source}")
    input_source: TaskOrganizer = task(source)
    records = [Material(**record) for _, record in input_source.formatted_records()]
    for record in tqdm(records):
        insert_into_material_table(record)

def show_dashboard():
    logger.info("show dashboard")

@dataclass
class Arguments:
    load: Optional[bool]
    dashboard: Optional[bool]
    source: Literal['source1', 'source2', 'source3']

def main():
    parser = argparse.ArgumentParser(prog='Vanilla Steel',
                                     description="A tool to collate all resources into a single dataset",
                                     epilog='Either run a load or show dashboard'
                                    )
    parser.add_argument("-l", "--load", action='store_true', help="specify if you want to run the load pipeline")
    parser.add_argument("-s", "--source", type=int, choices=[1, 2, 3], help="specify the source to load the data from")
    parser.add_argument("-d", "--dashboard", action='store_true', help="specify if you want to show the dashboard")
    args: Arguments = parser.parse_args()
    match args.__dict__:
        # ======================================================================
        case {'load': True, 'source': 1}:
            """
                Run load data for source 1
            """
            load_data(InputSource1, './resources/source1.xlsx')

        case {'load': True, 'source': 2}:
            """
                Run load data for source 2
            """
            load_data(InputSource2, './resources/source2.xlsx')

        case {'load': True, 'source': 3}:
            """
                Run load data for source 3
            """
            load_data(InputSource3, './resources/source3.xlsx')

        case {'dashboard': True}:
            """
                Show Dashboard
            """
            show_dashboard()
        case _:
            parser.print_help()
            raise ArgumentError("wrong combination of options selected !!!")

if __name__ == "__main__":
    main()

