# -*- coding: utf-8 -*-
"""
flexible_config
~~~~~~~~~~~~~~~

Supports loading configuration from the current environment or from a config file $HOME/.cloudconnect.
Useful for keeping per-env configuration in one place in your development environment, while using
ENV vars when deployed on Heroku.

Usage
-----

running flexible_config loads settings from ENV or the config file into the current globals() dict.
Thus recommended usage is to add to the end of your settings.py:

REQUIRED_OPTIONS = ['opt1', 'opt2', ...]
OPTIONS_OPTIONS = ['opt3', 'opt4', ...]

execfile("./lib/flexible_config.py")

flexible_config will look for REQUIRED_OPTIONS and OPTIONAL_OPTIONS in the current globals() dict
and will import found keys from os.environ. Any settings found in $HOME/.cloudconnect will also
be imported.

Missing values from REQUIRED_OPTIONS will be reported.

Configuration file
------------------
Your .cloudconnect file follows python ConfigParser syntax. In particular, you can have separate sections
per environment:

    [dev]
    opt1=
    opt2=
    [prod]
    opt1=
    opt2=

By default we will load the "dev" section. Set CCENV to load a different section.


"""

from setuptools import setup

setup(
    name='flexible_config',
    version='0.1',
    url='https://github.com/cloudconnect/flexible_config.git',
    license='BSD',
    author='Scott Persinger',
    author_email='scottpersinger@gmail.com',
    description='Read config from the environment or a multi-env config file.',
    long_description=__doc__,
    py_modules=['flexible_config'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
