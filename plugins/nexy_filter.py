import re
import logging
from Nexy.db import DB

logger = logging.getLogger('nexy.plugins.filter')

def filter(cmd, db):
	logger.debug('Looking for plugin for input: "{}"'.format(cmd))
	all_filters = get_all_filters(db)
	matched_filter = match_command_against_filters(all_filters, cmd)
	if matched_filter is not None:
		plugin_name = get_plugin_name_from_matched_filter(matched_filter)
		return plugin_name
	return None

def get_all_filters(db):
	return db.findAll('filter')

def match_command_against_filters(filters, cmd):
	for f in filters:
		logger.debug("Searching in filter: {} --- {}".format(f['id'], f['phrase']))
		if re.search(f['phrase'], cmd, re.IGNORECASE):
			logger.debug("Matched {} on {}".format(cmd, f['phrase']))
			return f

def get_plugin_name_from_matched_filter(f):
	return f['id']