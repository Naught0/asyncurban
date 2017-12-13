class Word:
    """ This is a basic data class which holds the UrbanDictionary API's
    response to a GET request

    It supports basic operations like str(), ==, and != """
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
