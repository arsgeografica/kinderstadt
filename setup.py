#!/usr/bin/env python

from setuptools import setup, find_packages
import versioneer


versioneer.VCS = 'git'
versioneer.versionfile_source = 'kinderstadt/_version.py'
versioneer.versionfile_build = 'kinderstadt/_version.py'
versioneer.tag_prefix = 'v'
versioneer.parentdir_prefix = 'kinderstadt-'


setup(
    name="kinderstadt",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    install_requires=[
        'django-cms==3.0.13',
        'Django==1.6.11',
        'psycopg2==2.6',
        'path.py==7.3',
        'djangocms-admin-style==0.2.5',
    ],
    extras_require={
        'devel': [
            'autopep8',
            'flake8',
        ]
    },
    entry_points={
        'console_scripts': [
            'kinderstadt = kinderstadt.cli:main',
        ],
    },
)
