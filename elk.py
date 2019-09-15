from loguru import logger
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from datetime import datetime

class ELK:
    "Wrapper Class for Logs in Elasticsearch"
    def __init__(self, ELK_URL, ELK_PORT):
        self.url = ELK_URL + ":" + ELK_PORT
    
    def _connect(self):
        es = Elasticsearch([self.url])
        return es

    def getLogs(self, SERVICE):
        """get the logs for a given service from the ELK stack
        
        Arguments:
            SERVICE {[string]} -- [Service name like stated in docker.name in the elk logs]
        
        Returns:
            [list] -- [last 10 entries of the given service]
        """
        logs = []
        SERVICE = "/" + SERVICE
        es = self._connect()
        s = Search(using=es, index="logstash") \
            .filter("match_phrase", docker__name=SERVICE) \
            .filter('range', **{'@timestamp':{'gte': 'now-5m' , 'lt': 'now'}})
        response = s.execute()
        logger.debug(response)
        for hit in response:
            logger.debug("{}: {}", hit.docker.name, hit.message)
            logs.append(hit.message)
        return logs

if __name__ == '__main__':
    logger.warning("Please run m0nitor.py")