from loguru import logger
from elasticsearch import Elasticsearch


class ELK:
    "Wrapper Class for Logs in Elasticsearch"
    def __init__(self, ELK_URL, ELK_PORT):
        self.url = ELK_URL + ":" + ELK_PORT
    
    def connect(self):
        es = Elasticsearch([self.url])
        return es

if __name__ == '__main__':
    e = ELK("192.168.42.167", "9200")
    info = e.connect()
    logger.debug(info.info())