from setuptools import setup, find_packages

setup(
    name = 'dstoolz',
    version = '0.1.0',
    # packages = find_packages(),  # Encuentra automáticamente `dstoolz`
    packages = ['dstoolz'], 
    install_requires = [],  # Dependencias necesarias, si las hay
    description = 'Data Science Tools',
    author = 'mardelmir',
    url = 'https://github.com/mardelmir/DSTools',
)