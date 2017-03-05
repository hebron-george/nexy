#! /usr/bin/env python
#
# Author: Hebron George
# Description: IRC Bot
# Date: March 4, 2017

""" An IRC bot.

"""

import irc.bot
import logging

class NexyBot(irc.bot.SingleServerIRCBot):
	pass

def main():
	logger = logging.getLogger()
	handler = logging.StreamHandler()
	formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
	handler.setFormatter(formatter)
	logger.addHandler(handler)
	logger.setLevel(logging.DEBUG)
	logger.debug("Hello World!")

if __name__ == "__main__":
	main()
