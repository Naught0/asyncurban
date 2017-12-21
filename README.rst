AsyncUrban
==========

|docs| |pypi|

Yet another UrbanDictionary API wrapper.

AsyncUrban is a non-blocking library, using asyncio and aiohttp, which
can be used to access UrbanDictionary data.

Installation
------------

Make sure you have Python3.5+ and run
``py -3 -m pip install asyncurban`` for Windows, or
``python3 -m pip install asyncurban`` for most other things.

Documentation
-------------

You can find the docs at http://asyncurban.readthedocs.io/ and a brief example below.

Examples
--------

.. code:: py

    >>> import asyncio
    >>> from asyncurban import UrbanDictionary
    >>> loop = asyncio.get_event_loop()
    
    # session and loop are optional kwargs for your convenience if 
    # You already have them defined for your project
    >>> urban = UrbanDictionary(loop=loop)

    # Get a word definition
    >>> word = loop.run_until_complete(urban.get_word('dank'))
    >>> word.definition
    'Also an expression requently used by stoners and hippies for something of high quality.'

    # Get a random word
    >>> random_word = loop.run_until_complete(urban.get_random())
    >>> print(random_word)
    Orgasm
    >>> random_word.definition
    "When a woman reaches their 'climax'. It is the most desirable feeling EVER. Its like an explosion inside the body that feels so good."

    # You can even search for X matching words and get a list
    # The default is 3 but can be specified
    >>> word_list = loop.run_until_complete(urban.search('test', limit=5))
    >>> print(word_list)
    [<Word word=test defid=708924>, <Word word=test defid=2957653>, <Word word=test defid=2573364>, <Word word=test defid=1876232>, <Word word=test defid=1662552>]
    >>> word_list[0].definition
    'A process for testing things'

Issues
------

Feel free to open up an issue or submit a PR if you have trouble or see a way to improve the code.

.. |docs| image:: https://readthedocs.org/projects/asyncurban/badge/?version=latest
    :target: http://asyncurban.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |pypi| image:: https://badge.fury.io/py/asyncurban.svg
      :target: https://badge.fury.io/py/asyncurban