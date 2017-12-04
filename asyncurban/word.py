class Word:
    def __init__(self, urban_dict: dict):
        self.defid = urban_dict['defid']
        self.word = urban_dict['word']
        self.author = urban_dict['author']
        self.link = urban_dict['permalink']
        self.definition = urban_dict['definition']
        self.examples = urban_dict['example']
        self.votes = {'up': urban_dict['thumbs_up'], 'down': urban_dict['thumbs_down']}
        self.current_vote = urban_dict['current_vote'] # This seems to always be an empty string

    def __str__(self):
        return self.word

    def __repr__(self):
        return '<Word word={0.word} defid={0.defid}>'.format(self)

    def __eq__(self, other):
        return isinstance(other, Word) and other.defid == self.defid

    def __ne__(self, other):
        return not self.__eq__(other)
