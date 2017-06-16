try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Determines if your panda is clean to do whatever analysis or model you see fit',
    'author': 'Ramiro Manso',
    'author_email': 'ramiro.manso@beeva.com',
    'version': '0.1',
    'packages': ['PandasDoctor'],
    'name': 'PandasDoctor'
}

setup(**config)
