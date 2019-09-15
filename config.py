import yaml
from loguru import logger

def load_config(config_file):
    try:
        with open(config_file, 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                logger.error(exc)
    except EnvironmentError as exc:
        data = dict(
            sonarr = dict(
                URL = '',
                API_KEY = '',
            ),
            elk = dict(
                URL = '#Enter the IP Adress of your Elasticsearch instance, eg. 192.168.100.1',
                PORT = '#Enter the port where your Elasticsearch instance listens, eg. 9200',
                SERVICES = '# Enter the services which should be delivered',
            )   
        )
        logger.error(exc)
        logger.info("Creating empty configuration file.")
        with open(config_file, 'w') as outfile:
            yaml.dump(data, outfile, default_flow_style=False)


if __name__ == '__main__':
    logger.info("Config Main Module - Just for testing!")
