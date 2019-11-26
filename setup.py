from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ipstack",
    version="0.1.4",
    author="Nathan Fiscaletti",
    author_email="nathan.fiscaletti@gmail.com",
    description="A Python library for interfacing with IPStack Geo API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nathan-fiscaletti/ipstackgeo-py",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
