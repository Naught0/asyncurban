class UrbanException(Exception):
    """Base exception for the rest.
    """
    pass


class WordNotFoundError(UrbanException):
    """Raised when the UrbanDictionary API does not return results for a word.

    Attributes
    ----------
    message : str
        A message which is displayed indicating the error and which word was not found.

    Parameters
    ----------
    word : str
        The word which was not found (user input).
    """
    def __init__(self, word: str):
        self.message = 'Unable to find word matching "{}"'.format(word)
        super().__init__(self.message)


class UrbanConnectionError(UrbanException):
    """Raised when the UrbanDictionary API raises a status != 200 (success).
    
    Attributes
    ----------
    message : str
        A message which is displayed indicating the error and response status.

    Parameters
    ----------
    http_status : int
        The status of the request which failed.
    """
    def __init__(self, http_status: int):
        self.status = http_status
        self.message = 'UrbanDictionary API failed to respond with status {}'.format(http_status)
        super().__init__(self.message)