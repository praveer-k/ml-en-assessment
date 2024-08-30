from pydantic import BaseModel, ConfigDict
# from pydantic.alias_generators import to_camel, to_pascal, to_snake

class TaskMetadata(BaseModel):
    model_config = ConfigDict(extra='forbid')
    
    source: str

class TaskScript(BaseModel):
    model_config = ConfigDict(extra='forbid')
    
    name: str
    module: str
    metadata: TaskMetadata

class Specification(BaseModel):
    model_config = ConfigDict(extra='forbid')

    task_scripts: list[TaskScript]
