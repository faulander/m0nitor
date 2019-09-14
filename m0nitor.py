import yaml
from loguru import logger
from config import load_config
from sonarr import Sonarr

config = load_config("m0nitor.yml")
print(config)
s = Sonarr(config['sonarr']['URL'], config['sonarr']['API_KEY'])
logger.debug(s.getLastEpisodes())
