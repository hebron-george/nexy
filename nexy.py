#! /usr/bin/env python
#
# Author: Hebron George
# Description: IRC Bot
# Date: March 4, 2017

""" An IRC bot.

"""
import irc.bot
import logging
from pluginbase import PluginBase
from ConfigParser import SafeConfigParser
from Nexy.db import DB

logging.basicConfig(filename='nexy.log', level=logging.DEBUG)

class NexyBot(irc.bot.SingleServerIRCBot):
	def __init__(self, serversConfig):
		logging.debug('Setting up nexy to connect to: {}...'.format(serversConfig))
		irc.bot.SingleServerIRCBot.__init__(self, [('irc.freenode.net', 6667)], 'nexy', 'nexy')
		self.channel = '#nexy'
		self.plugin_base = PluginBase(package='nexy.plugins')
		self.plugin_source = self.plugin_base.make_plugin_source(searchpath=['./plugins'])
		self.db = DB()

	def on_nicknameinuse(self, c, e):
		c.nick(c.get_nickname() + "_")

	def on_welcome(self, c, e):
		c.join(self.channel)

	def on_privmsg(self, c, e):
		self.do_command(e, e.arguments[0])

	def on_pubmsg(self, c, e):
		a = e.arguments[0].split(" ", 1)
		if len(a) > 1 and irc.strings.lower(a[0]) == irc.strings.lower(self.connection.get_nickname()):
			self.do_command(e, a[1].strip())
		return

	def on_dccmsg(self, c, e):
		# non-chat DCC messages are raw bytes; decode as text
		text = e.arguments[0].decode('utf-8')
		c.privmsg("You said: " + text)

	def on_dccchat(self, c, e):
		if len(e.arguments) != 2:
			return
		args = e.arguments[1].split()
		if len(args) == 4:
			try:
				address = ip_numstr_to_quad(args[2])
				port = int(args[3])
			except ValueError:
				return
			self.dcc_connect(address, port)

	def do_command(self, e, cmd):
		nick = e.source.nick
		c = self.connection
		logging.debug("event = {}".format(e))
		logging.debug("cmd = {}".format(cmd))

		if cmd == "disconnect":
			self.disconnect()
		elif cmd == "die":
			self.die()
		elif cmd == "stats":
			for chname, chobj in self.channels.items():
				c.notice(nick, "--- Channel statistics ---")
				c.notice(nick, "Channel: " + chname)
				users = sorted(chobj.users())
				c.notice(nick, "Users: " + ", ".join(users))
				opers = sorted(chobj.opers())
				c.notice(nick, "Opers: " + ", ".join(opers))
				voiced = sorted(chobj.voiced())
				c.notice(nick, "Voiced: " + ", ".join(voiced))
		elif cmd == "dcc":
			dcc = self.dcc_listen()
			c.ctcp("DCC", nick, "CHAT chat %s %d" % (
				ip_quad_to_numstr(dcc.localaddress),
				dcc.localport))
		elif cmd == "version":
			v = self.get_version()
			c.notice(nick, "{}".format(v))
		else:
			try:
				plugin_name = self.get_plugin_name(cmd)
				if plugin_name == None:
					raise ImportError('get_plugin_name() returned None for input: {}'.format(cmd))
				logging.debug("Got plugin_name = {}".format(plugin_name))
				plugin = self.plugin_source.load_plugin(plugin_name)
				logging.debug("This is the plugin that was loaded: {}".format(plugin))
				plugin.run(e, c)
			except ImportError:
				c.notice(nick, "--- [nexy] help ---")
				c.notice(nick, "To make me do something, try: nexy <command>")
				c.notice(nick, "Some common commands:")
				c.notice(nick, "quote - opme - weather <zip>")

	def get_plugin_name(self, cmd):
		filter_plugin = self.plugin_source.load_plugin('nexy_filter')
		plugin_name = filter_plugin.filter(cmd, self.db)
		if plugin_name == "" or plugin_name is None:
			return None
		return plugin_name

def main():

	conf = SafeConfigParser()
	conf.read('config/servers.ini')

	#logger.debug('Connecting to servers: {}'.format(conf.sections()))
	serverPortPairs = getServerPortPairs(conf)

	nexy = NexyBot(serverPortPairs)

	nexy.start()
	logging.debug("Starting nexy...")

def setupLogger():
	logger = logging.getLogger('nexy')
	handler = logging.StreamHandler()
	formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
	handler.setFormatter(formatter)
	logger.addHandler(handler)
	logger.setLevel(logging.DEBUG)

def getServerPortPairs(conf):
	logger = logging.getLogger('nexy.getServerPortPairs')
	arrayOfServerPortTuples = []
	for each_section in conf.sections():
		for (k, v) in conf.items(each_section):
			if k == 'server':
				server = v
			elif k == 'port':
				port = v

		if port is None:
			port = 6667
		if server is None:
			logger.error('Missing server in config section: {}').format(each_section)
			exit()

		arrayOfServerPortTuples.append((server, port))

	return arrayOfServerPortTuples


if __name__ == "__main__":
	#setupLogger()
	logger = logging.getLogger('nexy')
	main()
