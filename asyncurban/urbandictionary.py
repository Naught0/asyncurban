import asyncio
from typing import List

import aiohttp

from .errors import *
from .word import Word


class UrbanDictionary:
    """A client which fetches word info from the UrbanDictionary API.
    
    Attributes
    ----------
    API_URL : str
        The base URL for all search requests.
    
    RANDOM_URL : str
        The base URL for random word requests. 

    Parameters
    ----------
    loop : asyncio.AbstractEventLoop, optional
        The asyncio loop in which the program runs. If one isn't provided, a loop is created. 
    
    session : aiohttp.ClientSession, optional
        The session which makes all calls to the API. If one isn't provided, a session is created. 
    """
    API_URL = 'http://api.urbandictionary.com/v0/define'
    RANDOM_URL = 'http://api.urbandictionary.com/v0/random'

    def __init__(self, loop: asyncio.AbstractEventLoop = None, session: aiohttp.ClientSession = None):
        self.loop = loop or asyncio.get_event_loop()
        self.session = session or aiohttp.ClientSession(loop=self.loop)

    async def _get(self, term: str = None, random: bool = False) -> dict:
        """Helper method to reduce some boilerplate with aiohttp 
        
        Parameters
        ----------
        term : str, optional
            The term to search for. Optional if doing a random search.
        
        random : bool, optional
            Whether the search should return a random word.
        
        Returns
        -------
        dict
            A dict representation of the JSON response from the API.
        
        Raises
        ------
        UrbanConnectionError
            If the response status isn't 200.
        
        WordNotFoundError
            If the response doesn't contain data (i.e. no word found). 
        """
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
            raise WordNotFoundError(term)

        return response

    async def get_word_raw(self, term: str) -> dict:
        """Gets the raw json response for a word"""
        pass

    async def search_raw(self, term: str, limit: int = 3) -> dict:
        """Gets the raw json response for a search"""
        pass

    async def get_word(self, term: str) -> Word:
        """Gets the first matching word available.
        
        Parameters
        ----------
        term : str
            The word to be defined.
        
        Returns
        -------
        Word
            The closest matching Word object from UrbanDictionary.

        Raises
        ------
        UrbanConnectionError
            If the response status isn't 200.

        WordNotFoundError
            If the response doesn't contain data (i.e. no word found).
        """
        resp = await self._get(term=term)
        return Word(resp['list'][0])

    async def search(self, term: str, limit: int = 3) -> List[Word]:
        """Performs a search for a term and returns a list.
        
        Parameters
        ----------
        term : str
            The term to be defined.
            
        limit : int, optional
            Max amount of results returned.

        Note
        ----
            The API will relay a fixed number of words and definitions, so ``limit`` can be arbitrarily high if needed or wanted. 
        
        Returns
        -------
        List[Word]
            A list of Word objects of up to the specified length.

        Raises
        ------
        UrbanConnectionError
            If the response status isn't 200.

        WordNotFoundError
            If the response doesn't contain data (i.e. no word found).
        """
        resp = await self._get(term=term)
        words = resp['list']
        return [Word(x) for x in words[:limit]]

    async def get_random(self) -> Word:
        """Gets a random Word.
        
        Returns
        -------
        Word
            A random Word object.
        """
        resp = await self._get(random=True)
        return Word(resp['list'][0])
