import random

def run(e, conn):
	print "Inside greetings run()!"
	greetings = get_greetings()
	conn.privmsg(e.target, "{}, {}!".format(random.choice(greetings), e.source.nick))

def get_greetings():
	return ['Hi', 'Hello', 'Greetings', 'Howdy', 'Hey', "What's up", "What's good", 'What up', 'Yo', 'Yoyo']