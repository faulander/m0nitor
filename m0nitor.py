import yaml
from loguru import logger
from config import load_config
from sonarr import Sonarr
from elk import ELK

config = load_config("m0nitor.yml")
print(config)
s = Sonarr(config['sonarr']['URL'], config['sonarr']['API_KEY'])
e = ELK(config['elk']['URL'], config['elk']['PORT'])
es = e.connect()
logger.debug(s.getLastEpisodes())
logger.debug(s.getDiskSpace())
logger.debug(es.info())