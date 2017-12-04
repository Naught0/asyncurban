from os import path
from distutils.core import setup

here = path.abspath(path.dirname(__file__))

try:
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ''

setup(
    name='AsyncUrban',
    packages=['AsyncUrban'],
    version='0.1.5',
    description='An asynchronous wrapper around the UrbanDictionary API.',
    long_description=long_description,
    author='James E',
    author_email='naught0@github.com',
    url='https://github.com/naught0/AsyncUrban',
    download_url='https://github.com/Naught0/AsyncUrban/archive/0.1.5.tar.gz',
    keywords=('dictionary', 'urban', 'urbandictionary', 'define'),
    install_requires=['aiohttp'],
    python_requires='>=3.5',
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ]
)
