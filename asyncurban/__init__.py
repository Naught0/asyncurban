from pkg_resources import get_distribution, DistributionNotFound

from .urbandictionary import UrbanDictionary
from .word import Word
from .errors import *

__title__ = 'asyncurban'
__author__ = 'naught0'
__license__ = 'MIT'

try:
    __version__ = get_distribution(__title__).version 
except:
    pass

__all__ = ('UrbanDictionary', 'Word')
