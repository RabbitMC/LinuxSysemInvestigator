# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='LinuxSysemInvestigator',
    version='0.0.1',
    description='Generic Linux System Investigator Kit',
    long_description=readme,
    author='Miralem Cebic',
    author_email='m.cebic@web.de',
    url='https://github.com/RabbitMC/LinuxSysemInvestigator',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)