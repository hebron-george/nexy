#! /usr/bin/env python
#
# Author: Hebron George
# Description: IRC Bot
# Date: March 4, 2017

""" An IRC bot.

"""

import irc.bot
import logging
from ConfigParser import SafeConfigParser

class NexyBot(irc.bot.SingleServerIRCBot):
	pass

def main():
	setupLogger()
	logger = logging.getLogger('nexy')

	conf = SafeConfigParser()
	conf.read('config/servers.ini')

	logger.debug('Connecting to servers: {}'.format(conf.sections()))

def setupLogger():
	logger = logging.getLogger('nexy')
	handler = logging.StreamHandler()
	formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
	handler.setFormatter(formatter)
	logger.addHandler(handler)
	logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
	main()
