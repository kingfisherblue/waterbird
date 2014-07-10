try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Orange Eternal Waterbird',
    'author': 'Flora Fong',
    'url': 'URL to get it at.',
    'download_url': 'https://github.com/ffong',
    'author_email': 'flora.lt.fong@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['waterbird'],
    'scripts': [],
    'name': 'waterbird'
}

setup(**config)