from typing import Dict


class Word:
    """A data class representing a word from the UrbanDictionary API
    
    .. table:: Available operations
        :widths: auto

        ==========  =========================================
        Operation   Result
        ==========  =========================================
        ``x == y``      Checks if two Words are equal
        ``x != y``      Checks if two Words are not equal
        ``str(x)``      Returns a string representation of a Word
        ==========  =========================================

    Attributes
    ----------
    defid : int
        The UrbanDictionary definition ID.
        
    word : str
        The actual word.
        
    author : str
        The author of the defintion contained in the object.
        
    link : str
        The link to the definition of the word.
        
    definition : str
        The definition of the word.
        
    examples : str
        User created examples of the word. Typically used in a sentence (or a few).
        
    votes : Dict[str, int]
        A dict containing both the upvotes and downvotes for this word and definition pair.

        .. code-block:: python3

            # Example structure
            {
                'up': 400,
                'down': 20
            }
        
    current_vote : str
        An inexplicably empty string as far as I can tell, but included in the API response nonetheless.
    """
    def __init__(self, urban_dict: dict):
        self.defid = urban_dict['defid']
        self.word = urban_dict['word']
        self.author = urban_dict['author']
        self.link = urban_dict['permalink']
        self.definition = urban_dict['definition']
        self.examples = urban_dict['example']
        self.votes = {'up': urban_dict['thumbs_up'], 'down': urban_dict['thumbs_down']}
        self.current_vote = urban_dict['current_vote'] # This seems to always be an empty string

    def __str__(self) -> str:
        return self.word

    def __repr__(self) -> str:
        return '<Word word={0.word} defid={0.defid}>'.format(self)

    def __eq__(self, other) -> bool:
        return isinstance(other, Word) and other.defid == self.defid
