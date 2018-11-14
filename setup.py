#!/usr/bin/env python

import os

from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setupOptions = dict(
    name='awsgen',
    version='0.0.16',
    install_requires=[
        'boto3>=1.9.35',
        'botocore>=1.12.16',
        'requests', 
        'configparser'
    ],
    include_package_data=True,
    scripts=[
        'bin/aws-gen', 
        'bin/aws-gen.cmd',
    ],
    provides=[],
    platforms=['Any'],
    namespace_packages=[],
    packages=find_packages(),
    license = "BSD",
    description = 'Manage AWS Security Token Service (STS)',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url = 'https://github.com/mvallim/aws-gen-cli',
    author='Marcos Vallim',
    author_email='tischer@gmail.com'
)

setup(**setupOptions)