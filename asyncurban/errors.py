class UrbanException(Exception):
    """ Base exception for the rest """
    pass


class WordNotFoundError(UrbanException):
    """ Raised when no results are found for a query """
    pass

class UrbanConnectionError(UrbanException):
    """ Raised when the UrbanDictionary API fails to respond """
    def __init__(self, http_status):
        self.status = http_status
        self.message = f'UrbanDictionary API failed to respond with status {http_status}'
        super().__init__(self.message)