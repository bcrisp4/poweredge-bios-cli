from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='poweredge-bios-cli',
    version='0.0.1',
    license='GNU General Public License v3.0',
    author='Ben Crisp',
    author_email='ben@thecrisp.io',
    description='A CLI for fetching BIOS attributes from Dell PowerEdge servers uisng the Redfish API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bcrisp4/poweredge-bios-cli',
    python_requires='>=3.6',
    install_requires=[
        'click',
        'requests'
    ],
    packages=[
        'poweredge_bios_cli',
    ],
    entry_points='''
        [console_scripts]
        poweredge-bios-cli=poweredge_bios_cli.cli:cli
    '''
)
