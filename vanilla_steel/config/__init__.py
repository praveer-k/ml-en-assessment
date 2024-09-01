from vanilla_steel.config.settings import Settings, Logger

# Initialize settings
# -----------------------------------------------------------------------
settings = Settings(_env_file=['.env', '../../.env'], _env_file_encoding='utf-8')
settings.DOCS.BUILD_DIR = ""
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
logger = Logger.getInstance()
logger.setLevel(settings.LOG_LEVEL.alias)
logger.info("Initialized Settings ...")
# Visible only when log level is set to DEBUG manually in logger.py file
logger.debug(settings.__dict__)
