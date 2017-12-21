.. asyncurban documentation master file, created by
   sphinx-quickstart on Thu Dec 21 03:19:09 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to asyncurban's documentation!
======================================

asyncurban is an asynchronous library which can be used to access UrbanDictionar word data easily. It provides a convenient layer of abstraction over the raw UrbanDictionary API.

Installation
------------

You can obtain the stable version of the package via pip.

.. code:: python3

   $ python3 -m pip install -U asyncurban

Otherwise, head over to https://github.com/naught0/asyncurban to check out the latest and greatest build.

Quickstart
----------

.. code:: py

    >>> import asyncio
    >>> from asyncurban import UrbanDictionary
    >>> loop = asyncio.get_event_loop()
    >>> run = loop.run_until_complete
    
    # session and loop are optional kwargs for your convenience if 
    # you already have them defined for your project
    >>> urban_client = UrbanDictionary(loop=loop)

    # Get a word definition
    >>> word = run(urban_client.get_word('dank'))
    >>> word.definition
    'Also an expression requently used by stoners and hippies for something of high quality.'

    # Get a random word
    >>> random_word = run(urban_client.get_random())
    >>> print(random_word)
    Orgasm
    >>> random_word.definition
    "When a woman reaches their 'climax'. It is the most desirable feeling EVER. Its like an explosion inside the body that feels so good."

    # You can even search for X matching words and get a list
    # The default is 3 but can be specified
    >>> word_list = run(urban_client.search('test', limit=5))
    >>> print(word_list)
    [<Word word=test defid=708924>, <Word word=test defid=2957653>, <Word word=test defid=2573364>, <Word word=test defid=1876232>, <Word word=test defid=1662552>]
    >>> word_list[0].definition
    'A process for testing things'

.. toctree::
   :name: Contents
   :maxdepth: 3

   ref

Indices and tables
~~~~~~~~~~~~~~~~~~

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
