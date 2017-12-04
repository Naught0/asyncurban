class AsyncUrbanException(Exception):
    """ Base exception for the rest """
    pass


class WordNotFoundError(Exception):
    """ Raised when no results are found for a query """
    pass
