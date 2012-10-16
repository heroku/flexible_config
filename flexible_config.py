# Can load config from either a local config file, or from the environment
import os
import os.path

def determine_env():
	if 'CCENV' in os.environ:
		return os.environ['CCENV']
	else:
		return "dev"

def cast_env_vars(value):
	if value == "True":
		return True
	elif value == "False":
		return False
	elif value == "None":
		return None
	elif isinstance(value, basestring):
		return str(value)
	else:
		return value

def load_local_config(required = [], optional = [], config_file = None):
	"""Loads config from ~/.cloudconnect and from os.environ, and merges values into current globals()"""
	from ConfigParser import SafeConfigParser
	config = SafeConfigParser()
	config.optionxform = str
	path = config_file or os.path.join(os.environ['HOME'], ".cloudconnect")
	new_config = {}

	if os.path.exists(path):
		if 'DEBUG_SETTINGS' in os.environ:
			print "Reading '%s'" % path
		config.read(path)

		env = determine_env()
		if env in config.sections():
			for key in config.options(env):
				val =config.get(env, key)
				if key in os.environ:
					val = os.environ[key]
				val = cast_env_vars(val)
				if 'DEBUG_SETTINGS' in os.environ:
					print "Setting %s to %s" % (key, str(val))
				new_config[key] = val

	for key in required:
		if key in os.environ:
			new_config[key] = cast_env_vars(os.environ[key])

	for key in optional:
		if key in os.environ:
			new_config[key] = cast_env_vars(os.environ[key])
	return new_config

def load_remote_heroku_config(required=None, remote_config = None):
	remote_config = None
	new_config = {}

	if not remote_config and 'HEROKU_REMOTE_CONFIG' in os.environ:
		remote_config = os.environ['HEROKU_REMOTE_CONFIG']

	if remote_config:
		if not required:
			raise Exception("Must pass required options if using HEROKU_REMOTE_CONFIG")
		parts = remote_config.split(":")
		if len(parts) < 2:
			raise Exception("Error, bad format for HEROKU_REMOTE_CONFIG. Should be key:app-name")
		key = parts[0]
		app = parts[1]
		import heroku
		h = heroku.from_key(key)
		h_app = h.apps[app]
		for key in required:
			if key in h_app.config.data:
				if 'DEBUG_SETTINGS' in os.environ:
					print "Importing %s from %s" % (key, app)
				val = h_app.config.data[key]
				new_config[key] = cast_env_vars(val)
				os.environ[key] = val
	return new_config


def check_required_options(required = [], source = {}):
	for key in required:
		if key not in source:
			print "!!!!!!!!!!!!!! WARNING: Missing required option '%s'" % key

