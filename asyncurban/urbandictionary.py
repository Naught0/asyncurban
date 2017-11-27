#!/bin/env python3.6

import asyncio
import aiohttp

from .errors import *
from .word import Word


class UrbanDictionary:
    def __init__(self, loop=None, session=None):
        self.loop = asyncio.get_event_loop() if loop is None else loop
        self.session = aiohttp.ClientSession(loop=self.loop) if session is None else session
        self.api_url = 'http://api.urbandictionary.com/v0/define'
        self.random_url = 'http://api.urbandictionary.com/v0/random'
        self.get_success_code = 200

    async def _get_resp(self, term: str = None, random: bool = False) -> dict:
        """ Helper method to reduce some boilerplate with aiohttp """
        if not random:
            params = {'term': term}
            async with self.session.get(self.api_url, params=params) as r:
                if r.status == self.get_success_code:
                    resp = await r.json()
                else:
                    raise ConnectionError(f'UrbanDictionary API failed to respond\nStatus {r.status}')

            if not resp['list']:
                raise WordNotFoundError(f'Word "{term}", not found')

        else:
            async with self.session.get(self.random_url) as r:
                if r.status == self.get_success_code:
                    resp = await r.json()
                else:                   
                    raise ConnectionError(f'UrbanDictionary API failed to respond\nStatus {r.status}')

        return resp

    async def get_word(self, term: str):
        """ Returns the closest matching Word object for a given query """
        resp = await self._get_resp(term=term)
        return Word(resp['list'][0])

    async def search(self, term: str, limit: int = 3):
        """ Returns a list of Word objects matching a given query (default 3) """
        resp = await self._get_resp(term=term)
        words = resp['list']
        return [Word(x) for x in words[:limit]]

    async def get_random(self):
        """ Returns a random Word object """
        resp = await self._get_resp(random=True)
        return Word(resp['list'][0])
