import asyncio
import aiohttp
from typing import List

from .errors import *
from .word import Word


class UrbanDictionary:
    """ A client which allows you to easily retrieve information from Urban Dictionary. 
    
    You may optionally pass an aiohttp.ClientSession and an asyncio loop """
    API_URL = 'http://api.urbandictionary.com/v0/define'
    RANDOM_URL = 'http://api.urbandictionary.com/v0/random'

    def __init__(self, loop=None, session=None):
        self.loop = asyncio.get_event_loop() if loop is None else loop
        self.session = aiohttp.ClientSession(loop=self.loop) if session is None else session

    async def _get_resp(self, term: str = None, random: bool = False) -> dict:
        """ Helper method to reduce some boilerplate with aiohttp """
        if random:
            params = None
            url = self.RANDOM_URL
        else:
            params = {'term': term}
            url = self.API_URL

        async with self.session.get(url, params=params) as response:
            if response.status == 200:
                response = await response.json()
            else:
                raise UrbanConnectionError(response.status)

        if not response['list']:
            raise WordNotFoundError(f'Word "{term}", not found')

        return response

    async def get_word(self, term: str) -> Word:
        """ Returns the closest matching Word object for a given query """
        resp = await self._get_resp(term=term)
        return Word(resp['list'][0])

    async def search(self, term: str, limit: int = 3) -> List[Word]:
        """ Returns a list of Word objects matching a given query (default 3) """
        resp = await self._get_resp(term=term)
        words = resp['list']
        return [Word(x) for x in words[:limit]]

    async def get_random(self) -> Word:
        """ Returns a random Word object """
        resp = await self._get_resp(random=True)
        return Word(resp['list'][0])
