from vanilla_steel.task_organizer.task_organizer import TaskOrganizer
from vanilla_steel.task_organizer.input_source_1 import InputSource1
from vanilla_steel.task_organizer.input_source_2 import InputSource2
from vanilla_steel.task_organizer.input_source_3 import InputSource3
from vanilla_steel.database.queries import insert_into_material_table, fetch_stats
from vanilla_steel.database.models import Material
from vanilla_steel.llm.categorizer import Categorizer
from vanilla_steel.config import logger, settings
from vanilla_steel.config.logger import LogLevel
from vanilla_steel.docs.__main__ import DocumentationBuilder
from pydantic.dataclasses import dataclass
from typing import Optional, Literal
from tqdm import tqdm
import os
import argparse
import subprocess

class ArgumentError(Exception):
    def __init__(self, message):            
        super().__init__(message)

@dataclass
class Arguments:
    debug: Optional[bool]
    # loader
    load: Optional[bool]
    source: Literal['source1', 'source2', 'source3']
    # dashboard
    dashboard: Optional[bool]
    build: Optional[bool]
    serve: Optional[bool]
    watch: Optional[bool]
    # categorize
    categorize: Optional[bool]

def load_data(task: TaskOrganizer, source: str):
    logger.info(f"load data {source}")
    input_source: TaskOrganizer = task(source)
    records = [Material(**record) for _, record in input_source.formatted_records()]
    for record in tqdm(records):
        insert_into_material_table(record)

def show_dashboard():
    logger.info("show dashboard")
    subprocess.run(["streamlit", "run", "./vanilla_steel/dashboard/__main__.py"])

def show_docs(args: Arguments):
    logger.info("show documentations")
    SCR_DIR = os.path.abspath(settings.DOCS.SOURCE_DIR)
    BLD_DIR = os.path.abspath(settings.DOCS.BUILD_DIR)
    CACHE_DIR = os.path.abspath(settings.DOCS.CACHE_DIR)
    logger.warning(f"Source dir: {SCR_DIR}")
    logger.warning(f"Build dir: {BLD_DIR}")
    logger.warning(f"Cache dir: {CACHE_DIR}")
    doc = DocumentationBuilder(src_dir=SCR_DIR, build_dir=BLD_DIR, cache_dir=CACHE_DIR)
    doc.download_dependencies()
    if args.build:
        doc.build()
    elif args.watch:
        doc.build().watch()
    elif args.serve:
        doc.build().serve()

def main():
    parser = argparse.ArgumentParser(prog='Vanilla Steel',
                                     description="A tool to collate all resources into a single dataset",
                                     epilog='Either run a load or show dashboard'
                                    )
    # dagta loader
    parser.add_argument("-l", "--load", action='store_true', help="specify if you want to run the load pipeline")
    parser.add_argument("-s", "--source", type=int, choices=[1, 2, 3], help="specify the source to load the data from")
    # categorizer
    parser.add_argument("-c", "--categorize", action='store_true', help="specify if you want to run categorizer")
    # dashboard
    parser.add_argument("-d", "--dashboard", action='store_true', help="specify if you want to show the dashboard")
    # docs
    parser.add_argument("-docs", "--docs", action='store_true', help="specify if you want to show documentation")
    parser.add_argument("--watch", action="store_true", help="Watch for changes in document source directory")
    parser.add_argument("--build", action="store_true", help="Build Sphinx docs")
    parser.add_argument("--serve", action="store_true", help="Start the document server")
    parser.add_argument("--debug", action="store_true", help="Change log level to debug", default=False)

    args: Arguments = parser.parse_args()
    
    settings.LOG_LEVEL = LogLevel.DEBUG if args.debug==True else settings.LOG_LEVEL
            
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

        case {'categorize': True}:
            """
                Run categorier pipeline
            """
            Categorizer().run()
            
        case {'dashboard': True}:
            """
                Show Dashboard
            """
            show_dashboard()
        case {'docs': True}:
            """
                Show Documentation
            """
            show_docs(args)
        case _:
            parser.print_help()
            raise ArgumentError("wrong combination of options selected !!!")

if __name__ == "__main__":
    main()

