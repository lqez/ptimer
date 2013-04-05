#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup  # NOQA


classifiers = [
    'Topic :: Utilities',
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'License :: OSI Approved :: MIT License',
]

setup(
    name='ptimer',
    version='0.1.0',
    py_modules=['ptimer'],
    author='Park, Hyunwoo',
    author_email='ez.amiryo' '@' 'gmail.com',
    maintainer='Park, Hyunwoo',
    maintainer_email='ez.amiryo' '@' 'gmail.com',
    url='http://github.com/lqez/ptimer',
    description='Yet another precision timer for Python ',
    classifiers=classifiers,
)
