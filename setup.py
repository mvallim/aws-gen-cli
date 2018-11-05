#!/usr/bin/env python

from setuptools import setup, find_packages
 
setupOptions = dict(
    name='awsgen',
    version='0.0.8',
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
    url = 'https://github.com/mvallim/aws-gen-cli',
    author='Marcos Vallim',
    author_email='tischer@gmail.com'
)

setup(**setupOptions)