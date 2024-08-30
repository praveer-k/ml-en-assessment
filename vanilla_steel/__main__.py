from vanilla_steel.core.task_organizer import TaskOrganizer, TaskOrganizerFactory
from vanilla_steel.core.plugin import PlugIn
from vanilla_steel.database.queries import insert_into_material_table
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
    # docs
    docs: Optional[bool]
    build: Optional[bool]
    serve: Optional[bool]
    watch: Optional[bool]
    # categorize
    categorize: Optional[bool]

def load_data(task: TaskOrganizer, source: str):
    logger.info(f"load data {source}")
    input_source: TaskOrganizer = task(source)
    logger.info(input_source)
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
    # data loader
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
            
    # ======================================================================
    if args.load and args.source in [1, 2, 3]:
        """
            Run load data for source 1
        """
        plugin = PlugIn()
        plugin.load("specifications.yaml")
        factory = TaskOrganizerFactory()
        source = f"InputSource{args.source}"
        factory.register(source, plugin.object[source].module)
        # load_data(factory.funcs[source], plugin.object[source].metadata["source"])

    elif args.categorize:
        """
            Run categorier pipeline
        """
        Categorizer().run()
            
    elif args.dashboard:
        """
            Show Dashboard
        """
        show_dashboard()
    elif args.docs:
        """
            Show Documentation
        """
        show_docs(args)
    else:
        parser.print_help()
        raise ArgumentError("wrong combination of options selected !!!")

if __name__ == "__main__":
    main()

