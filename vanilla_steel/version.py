import json
import click
from urllib.parse import urlparse, ParseResult
from urllib.request import url2pathname
from vanilla_steel.config import logger
from importlib.metadata import version as pkg_version, distribution as pkg_distribution

PKG_IMPORT_NAME = "vanilla_steel"
PKG_NAME = "vanilla_steel"
__version__ = pkg_version(PKG_NAME)
PKG_REQUIREMENT = f"{PKG_NAME}=={__version__}"

def get_installed_requirement_string(package: str = PKG_NAME) -> str:
    """Gets the path of currently installed pakage"""
    # PEP 610 https://packaging.python.org/en/latest/specifications/direct-url/#specification
    dist = pkg_distribution(package)
    direct_url = dist.read_text("direct_url.json")
    if direct_url is not None:
        url: ParseResult = urlparse(json.loads(direct_url)["url"])
        if url.scheme == "file":
            return url2pathname(url.path)
    
    if package == PKG_NAME:
        package_requirement = PKG_REQUIREMENT
    else:
        package_requirement = f"{package}=={pkg_version(package)}"
    return package_requirement

@click.command(name="version", help="show package version")
def show_version():
    logger.info(PKG_REQUIREMENT)