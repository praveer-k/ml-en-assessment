import os
from enum import Enum
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from vanilla_steel.config.logger import LogLevel, Logger

class DocSettings(BaseModel):
    TITLE: str
    DESCRIPTION: str
    VERSION: str
    SOURCE_DIR: str
    BUILD_DIR: str
    CACHE_DIR: str
    PLANTUML_JAR: str

    class Config:
        frozen = True 

class DBSettings(BaseModel):
    HOST: str
    PORT: int
    USER: str
    EMAIL: str
    PASSWORD: str
    NAME: str

    @property
    def CONNECTION_STRING(self):
        return f"postgresql+psycopg2://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.NAME}"
    
    class Config:
        frozen = True 

class Environment(Enum):
    DEVELOPMENT = "dev"
    TESTING = "test"
    STAGING = "stage"
    PRODUCTION = "prod"

    class Config:
        frozen = True 

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_nested_delimiter='__', 
        env_nested_mapping=True, 
        case_sensitive=True, 
        env_file=('../.env'), 
        env_file_encoding='utf-8',
        extra='ignore',
        frozen=True
    )
    ENVIRONMENT: Environment
    LOG_LEVEL: LogLevel
    
    DOCS: DocSettings
    DB: DBSettings
    
    @property
    def PREFIX(self):
        match self.ENVIRONMENT:
            case Environment.DEVELOPMENT:
                return f"dev_"
            case Environment.TESTING:
                return f"tst_"
            case Environment.STAGING:
                return f"stg_"
            case _:
                return ""
    
    def __init__(self, *args, **kwargs):
        # check if environment variables `ENVIRONMENT` is set
        if "ENVIRONMENT" not in os.environ:
            logger = Logger.getInstance()
            logger.warning("ENVIRONMENT is not set")
            logger.warning("Setting ENVIRONMENT variable to `dev`")
            os.environ["ENVIRONMENT"] = "dev"
        super().__init__(*args, **kwargs)
