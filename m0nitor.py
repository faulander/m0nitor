import yaml
from loguru import logger
from config import load_config
from sonarr import Sonarr
from elk import ELK

config = load_config("m0nitor.yml")
print(config)
s = Sonarr(config['sonarr']['URL'], config['sonarr']['API_KEY'])
e = ELK(config['elk']['URL'], config['elk']['PORT'])
services = config['elk']['SERVICES']
logger.debug("Configured services: {}", services)
for service in services:
    logs = e.getLogs(service)
    for log in logs:
        logger.debug("Docker - {} - {}", service, log)
for episode in s.getLastEpisodes():
        logger.debug("Sonarr - {}", episode)
for pfad in s.getDiskSpace():
        logger.debug("Sonarr - {}", pfad)
