from setuptools import setup, find_packages

setup(
    name='telqtest1',
    version='0.0.4',
    description='Testing deployment to pypi',
    packages=find_packages(),
    install_requires = ['requests']
)