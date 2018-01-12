import asyncio
from typing import List

import aiohttp

from .errors import *
from .word import Word


class UrbanDictionary:
    """A client which fetches word info from the UrbanDictionary API.
    
    Attributes:
        API_URL (str): The base URL for all search requests.
        RANDOM_URL (str): The base URL for random word requests. 
    
    Args:
        loop (:class:`asyncio.AbstractEventLoop`, optional): The event loop in which the client runs. 
            If one isn't provided, a loop is created.  
        session (:class:`aiohttp.ClientSession`, optional): The session which makes all calls to the API. 
            If one isn't provided, a session is created. 
    """
    API_URL = 'http://api.urbandictionary.com/v0/define'
    RANDOM_URL = 'http://api.urbandictionary.com/v0/random'

    def __init__(self, loop: asyncio.AbstractEventLoop = None, session: aiohttp.ClientSession = None):
        if loop is None:
            self.loop = asyncio.get_event_loop()
            self.loop_provided = True
        else:
            self.loop = loop
            self.loop_provided = False

        if session is None:
            self.session = aiohttp.ClientSession(loop=self.loop)
            self.session_provided = True
        else:        
            self.session = session
            self.session_provided = False

    async def _get(self, term: str = None, random: bool = False) -> dict:
        """Helper method to reduce some boilerplate with :module:`aiohttp`.
        
        Args:
            term (str, optional): The term to search for. Optional if doing a random search.
            random (bool, optional): Whether the search should return a random word.
        
        Returns:
            :class:`dict`: A dict representation of the JSON response from the API.
        
        Raises:
            UrbanConnectionError: If the response status isn't ``200``.
            WordNotFoundError: If the response doesn't contain data (i.e. no word found). 
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

    async def get_word(self, term: str) -> Word:
        """Gets the first matching word available.
        
        Args:
            term (str): The word to be defined.
        
        Returns:
            :class:`Word`: The closest matching :class:`Word` object from UrbanDictionary.
        
        Raises:
            UrbanConnectionError: If the response status isn't ``200``.
            WordNotFoundError: If the response doesn't contain data (i.e. no word found).
        """
        resp = await self._get(term=term)
        return Word(resp['list'][0])

    async def search(self, term: str, limit: int = 3) -> List[Word]:
        """Performs a search for a term and returns a list of possible matching :class:`Word`\s.
        
        Args:
            term (str): The term to be defined.
        
            limit (int, optional): Max amount of results returned.
                Defaults to 3.
        
        Note:
            The API will relay a fixed number of words and definitions, so ``limit`` can be arbitrarily high if needed or wanted. 
        
        Returns:
            List[:class:`Word`]: A list of Word objects of up to the specified length.
        
        Raises:
            UrbanConnectionError: If the response status isn't ``200``.
            WordNotFoundError: If the response doesn't contain data (i.e. no word found).
        """
        resp = await self._get(term=term)
        words = resp['list']
        return [Word(x) for x in words[:limit]]

    async def get_random(self) -> Word:
        """Gets a random :class:`Word`.
        
        Returns:
            :class:`Word`: A random Word object.
                   
        Raises:
            UrbanConnectionError: If the response status isn't ``200``.
        """
        resp = await self._get(random=True)
        return Word(resp['list'][0])

    async def get_word_raw(self, term: str) -> dict:
        """Gets the raw json response for a word.
        
        Args:
            term (str): The word to be defined.
        
        Returns:
            :class:`dict`: The raw JSON response from the UrbanDictionary API for a particular word.
        
        Raises:
            UrbanConnectionError: If the response status isn't ``200``. 
            WordNotFoundError: If the response doesn't contain data (i.e. no word found).
        """
        return (await self._get(term=term))['list'][0]

    async def search_raw(self, term: str, limit: int = 3) -> List[dict]:
        """Performs a search for a term and returns the raw response.
        
        Args:
            term (str): The term to be defined.
            limit (int, optional): The maximum amount of results you'd like.
                Defaults to 3.
        
        Returns:
            List[:class:`dict`]: A list of :class:`dict`\s which contain word / definition information.
        """
        return (await self._get(term=term))['list'][:limit]

    async def get_random_raw(self) -> dict:
        """Gets a random word in raw json format.
        
        Returns:
            dict: The json representation of a random word as a :class:`dict`.

        Raises:
            UrbanConnectionError: If the response status isn't ``200``.
        """
        return (await self._get(random=True))['list'][0]

    async def close(self):
        """Closes the :class:`UrbanDictionary` client."""
        if self.session_provided:
            await self.session.close()
        if self.loop_provided:
            self.loop.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

