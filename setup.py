#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

import kombu_fernet

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'kombu_fernet',
    'kombu_fernet.serializers',
]

requires = [
    'anyjson>=0.3.3',
    'cryptography>=0.4',
    'kombu>=3.0.16',
]

with open('README.rst') as f:
    readme = f.read()
with open('LICENSE') as f:
    license = f.read()

setup(
    name='kombu-fernet-serializers',
    version=kombu_fernet.__version__,
    description='Symmetrically encrypted serializers for Kombu',
    long_description=readme,
    author='David Gouldin',
    author_email='dgouldin@heroku.com',
    url='https://github.com/heroku/kombu-fernet-serializers',
    packages=packages,
    package_data={'': ['LICENSE']},
    include_package_data=True,
    install_requires=requires,
    license=license,
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
    entry_points={
        'kombu.serializers': [
            'fernet_json = kombu_fernet.serializers.json:register_args',
            'fernet_yaml = kombu_fernet.serializers.yaml:register_args',
            'fernet_pickle = kombu_fernet.serializers.pickle:register_args',
            'fernet_msgpack = kombu_fernet.serializers.msgpack:register_args',
        ]
    }
)
