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
                API_KEY = ''
            )
        )
        logger.error(exc)
        logger.info("Creating empty configuration file.")
        with open(config_file, 'w') as outfile:
            yaml.dump(data, outfile, default_flow_style=False)


if __name__ == '__main__':
    logger.info("Config Main Module - Just for testing!")
