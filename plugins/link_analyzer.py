from urllib2 import urlopen
from lxml.html import parse
from lxml import etree
import logging

log = logging.getLogger("nexy.plugins.link_analyzer")

def run(e, conn):
	log.debug("In link_analyzer.run()")
	url = e.arguments[0].split()[1]
	title = get_url_title(url)
	log.debug("Got title: {}".format(title))
	msg_type = e.type
	if msg_type == "privmsg":
		target = e.source.nick
	else:
		target = e.target

	msg = "Title: {}".format(title)
	conn.privmsg(target, msg)

def get_url_title(url):
	try:
		page = urlopen(url)
		p = parse(page)
		return ''.join(p.find(".//title").text.decode('utf-8').strip().splitlines())
	except Exception as e:
		log.error("Exception thrown trying to get url's title: {}".format(url))
		log.error("{}".format(e))