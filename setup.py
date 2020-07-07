import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "jaygents",
    version = "0.0.1",
    author = "Jacob Valdez",
    author_email = "jacobfv@msn.com",
    description = ("Some personal reinforcement learning agent implimentations"),
    license = "MIT",
    keywords = "reinforcement learning",
    url = "http://packages.python.org/jaygents",
    packages=['jaygents'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
