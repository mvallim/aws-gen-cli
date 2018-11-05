#!/usr/bin/env python

from setuptools import setup, find_packages
 
setupOptions = dict(
    name='awsgen',
    version='0.0.3',
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
    url = 'https://bitbucket.org/mvallim_ciandt/aws-gen-cli',
    author='Marcos Vallim',
    author_email='tischer@gmail.com'
)

setup(**setupOptions)