import yaml
import json
from loguru import logger
from config import load_config
from sonarr import Sonarr
from elk import ELK
from flask import Flask, render_template


config = load_config("m0nitor.yml")
content = dict()
#print(config)
s = Sonarr(config['sonarr']['URL'], config['sonarr']['API_KEY'])
e = ELK(config['elk']['URL'], config['elk']['PORT'])
services = config['elk']['SERVICES']
#logger.debug("Configured services: {}", services)
for service in services:
    logs = e.getLogs(service)
    content[service] = logs

#logger.debug("Sonarr - {}", episode)
content['sonarr'] = s.getLastEpisodes()
content['diskspace'] = s.getDiskSpace()
logger.debug(content)


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('m0nitor.html', data=content)
