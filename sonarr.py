import requests
import json
from loguru import logger
import sys

class Sonarr:
    'Class to get data from sonarr'
    def __init__(self, SONARR_API_URL, SONARR_API_KEY, SONARR_API_PAGESIZE=10):
        self.url = SONARR_API_URL
        self.key = SONARR_API_KEY
        self.pagesize = SONARR_API_PAGESIZE


    def _getRawData(self, SONARR_API_ENDPOINT):
        """INTERNAL USE ONLY: Gets raw JSON Data from Sonarr
        
        Returns:
            [JSON] -- [raw JSON Output]
        """
        SONARR_INTERNAL_API_ENDPOINT = self.url + SONARR_API_ENDPOINT + "?sortKey=date&apikey=" + self.key + "&pagesize=" + str(self.pagesize) + "&sortdir=desc"
        logger.debug("API Endpoint: {}", SONARR_INTERNAL_API_ENDPOINT)
        try:
            r = requests.get(SONARR_INTERNAL_API_ENDPOINT)
        except ConnectionError:
            logger.error('Connection Error, please check your settings!')
            sys.exit(0)
        return r.json()


    def getLastEpisodes(self):
        """gets a list of the last downloaded episodes
        
        Returns:
            [list] -- [Show - SSeasonnumberEEpisodenumber - Episode Title]
        """
        lstLastEpisodes = []
        raw = self._getRawData("/history")
        for r in raw['records']:
            if len(str(r['episode']['seasonNumber'])) == 1:
                tmpSeasonNumber = "0" + str(r['episode']['seasonNumber'])
            if len(str(r['episode']['episodeNumber'])) == 1:
                tmpEpisodeNumber = "0" + str(r['episode']['episodeNumber'])
            tmpTitle = r['series']['title']
            tmpEpisode =  r['episode']['title']
            tmpQuality = r['quality']['quality']['name']
            ep =  tmpTitle + " - S" + tmpSeasonNumber + "E" + tmpEpisodeNumber + " - " + tmpEpisode + " (" + tmpQuality + ")"
            lstLastEpisodes.append(ep)
        return lstLastEpisodes


    def getDiskSpace(self):
        """returns the percentage of free disk space for all attached drives
        
        Returns:
            [list] -- [drive:percentage]
        """
        lstDiskSpace = []
        raw = self._getRawData('/diskspace')
        for r in raw:
            tmpPath = r['path']
            tmpFree = str(round((int(r['freeSpace']) / int(r['totalSpace'])) * 100))
            lstDiskSpace.append(tmpPath + ":" + tmpFree + "%")
            #logger.debug (tmpFree)
        return lstDiskSpace


    def getSystemStatus(self):
        raw = self._getRawData('/system/status')
        return raw


if __name__ == '__main__':
    logger.info("Sonarr Main Module - Just for testing!")
