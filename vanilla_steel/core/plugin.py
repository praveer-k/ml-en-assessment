import yaml
import importlib
from yaml import Loader
from typing import Any
from collections.abc import Callable
from pydantic.dataclasses import dataclass
from pydantic import ValidationError
from vanilla_steel.core.task_specification import Specification

@dataclass
class PlugInObject:
    module: Callable[..., Any]
    metadata: dict
    
class PlugIn:
    def __init__(self) -> None:
        self.object: dict[str, PlugInObject] = {}
    
    def load(self, specs_file: str) -> None:
        with open(specs_file) as f:
            content = f.read()
            values = Specification(**yaml.safe_load(content))
            for task_script in values.task_scripts:
                metadata = task_script.metadata.model_dump()
                module = importlib.import_module(name=task_script.module).__dict__[task_script.name]
                self.object[task_script.name] = PlugInObject(module=module, metadata=metadata)

