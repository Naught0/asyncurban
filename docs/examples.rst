.. currentmodule:: lolrune

.. _examples:

Examples
--------

The default interface is object oriented, so you can access attributes with dotted notation.

.. code:: py

  import asyncio

  from asyncurban import UrbanDictionary


  async def test(loop):
      ud = UrbanDictionary(loop=loop)

      word = await ud.get_word('dank')
      print('{0.word}: {0.definition}\n{0.permalink}'.format(word), end='\n\n')

      random_word = await ud.get_random()
      print('{0.word}: {0.definition}\n{0.permalink}'.format(random_word), end='\n\n')

      search_results = await ud.search('cowboy')
      print(search_results)

      await ud.close()

  if __name__ == '__main__':
      loop = asyncio.get_event_loop()
      loop.run_until_complete(test(loop))


Outputs

.. code-block:: text

  Dank: Also an expression requently used by stoners and hippies for something of high quality.
  http://dank.urbanup.com/1199991

  Chubby Chaser: someone who is attracted to chubby people.
  http://chubby-chaser.urbanup.com/2836416

  [<Word word='cowboy' defid=303986>, <Word word='cowboy' defid=1110260>, 
  <Word word='cowboy' defid=379273>]

You may also get a raw response in JSON/:class:`dict` format like so:

.. code:: py

  async def test_raw(loop):
      ud = UrbanDictionary(loop=loop)

      word = await ud.get_word_raw('dank')
      print(json.dumps(word, indent=2), end='\n\n')

      random_word = await ud.get_random_raw()
      print(json.dumps(random_word, indent=2), end='\n\n')

      search_results = await ud.search_raw('cowboy')
      print(json.dumps(search_results, indent=2))

      await ud.close()

  if __name__ == '__main__':
      loop = asyncio.get_event_loop()
      loop.run_until_complete(test_raw(loop))

Which outputs

.. code-block:: javascript

  {
    "definition": "Also an expression requently used by stoners and hippies for something of high quality.",
    "permalink": "http://dank.urbanup.com/1199991",
    "thumbs_up": 20560,
    "author": "Casey",
    "word": "Dank",
    "defid": 1199991,
    "current_vote": "",
    "example": "That borritos was dank, man.  \r\nor... That borritos was the dankness",
    "thumbs_down": 8063
  }

  {
    "definition": "Abbreviation for: you only live once\r\nThe dumbass's excuse for something stupid that they did\r\nAlso one of the most annoying abbreviations ever....",
    "permalink": "http://yolo.urbanup.com/6688179",
    "thumbs_up": 32255,
    "author": "shlubster",
    "word": "Yolo",
    "defid": 6688179,
    "current_vote": "",
    "example": "Guy 1: \"Hey i heard u got that girl pregnant\"\n\nDumbass 1: \"a man but hey YOLO\"\n\nGuy 1: \"Hey i heard that you broke ur leg falling off he balcony at that party\"\r\nDumbass 1: \"Ya but hey YOLO\"",
    "thumbs_down": 9024
  }

  [
    {
      "definition": "A cowboy is the ideal American figure because he comes packing with two Colt .45 Revolvers, and a double barrel shotgun, plus a 1HP...Horse.",
      "permalink": "http://cowboy.urbanup.com/303986",
      "thumbs_up": 847,
      "author": "Border Brother",
      "word": "cowboy",
      "defid": 303986,
      "current_vote": "",
      "example": "It'd be cool if I was a cowboy.",
      "thumbs_down": 296
    },
    {
      "definition": "A cute farmer boy who knows how to treat a lady!",
      "permalink": "http://cowboy.urbanup.com/1110260",
      "thumbs_up": 764,
      "author": "lil_miss_cowgirl",
      "word": "cowboy",
      "defid": 1110260,
      "current_vote": "",
      "example": "Save a horse, ride a cowboy",
      "thumbs_down": 411
    },
    {
      "definition": "The famous image of Americans.  The person who is poetic, a fighter, and can survive on his own. I have been called a cowboy before, by those without these skills",
      "permalink": "http://cowboy.urbanup.com/379273",
      "thumbs_up": 496,
      "author": "Grahamman",
      "word": "cowboy",
      "defid": 379273,
      "current_vote": "",
      "example": "John Wayne could stare down an army.\r\n\r\nOf course, he was a cowboy",
      "thumbs_down": 271
    }
  ]