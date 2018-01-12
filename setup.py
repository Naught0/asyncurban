from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='asyncurban',
    packages=['asyncurban'],
    use_scm_version={
        'version_scheme': 'guess-next-dev',
        'local_scheme': 'dirty-tag'
    },
    setup_requires=['setuptools_scm'],
    license='MIT',
    description='An asynchronous wrapper around the UrbanDictionary API.',
    long_description=long_description,
    author='James E',
    author_email='naught0@github.com',
    url='https://github.com/naught0/asyncurban',
    keywords=('dictionary', 'urban', 'urbandictionary', 'define'),
    install_requires=['aiohttp>=2.3.7'],
    python_requires='>=3.5',
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ]
)
