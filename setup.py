from os import path
from distutils.core import setup

long_description = ''
with open('README.rst') as f:
    long_description = f.read()

setup(
    name='asyncurban',
    packages=['asyncurban'],
    version='0.1.9',
    description='An asynchronous wrapper around the UrbanDictionary API.',
    long_description=long_description,
    author='James E',
    author_email='naught0@github.com',
    url='https://github.com/naught0/asyncurban',
    download_url='https://github.com/Naught0/asyncurban/archive/0.1.9.tar.gz',
    keywords=('dictionary', 'urban', 'urbandictionary', 'define'),
    install_requires=['aiohttp'],
    python_requires='>=3.5',
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ]
)
