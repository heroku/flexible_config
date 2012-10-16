flexible_config
~~~~~~~~~~~~~~~

Supports loading configuration from the current environment or from a config file $HOME/.cloudconnect.
Useful for keeping per-env configuration in one place in your development environment, while using
ENV vars when deployed on Heroku.

Usage
-----

    import flexible_config

	REQUIRED_OPTIONS = ['opt1', 'opt2', ...]
	OPTIONAL_OPTIONS = ['opt3', 'opt4', ...]

    globals().update(flexible_config.load_local_config(REQUIRED_OPTIONS, OPTIONAL_OPTIONS)

To load from a remote Heroku app's config:

	HEROKU_CONF = "<heroku key>:<heroku app name>"
    globals().update(flexible_config.load_remote_heroku_config(HEROKU_CONF))

TO check for required options:

    flexible_config.check_required_options(REQUIRED_OPTIONS, globals())

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


Installation
------------

Installation is simple too::

    $ pip install git+git@github.com:cloudconnect/flexible_config.git
