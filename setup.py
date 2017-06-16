try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Determines if your panda is clean to do whatever analysis or model you see fit',
    'author': 'Ramiro Manso',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'ramiro.manso@beeva.com',
    'version': '0.1',
    'install_requires': ['unittest, pandas, numpy'],
    'packages': ['PandasDoctor'],
    'name': 'PandasDoctor'
}

setup(**config)
