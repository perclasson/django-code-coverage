import sys
import os

from setuptools import setup

setup_kwargs = dict(
    name='trail',
    version='0.1',
    license='BSD',
    packages=['trail'],
    package_dir={'trail': 'trail'},
    entry_points={
        'console_scripts': ['trail=trail.main:main'],
    },
    install_requires=['wrapt>=1.10.5'],
)

setup(**setup_kwargs)
