
def run(e, conn):
	msg_type = e.type
	if msg_type == "privmsg":
		target = e.source.nick
	else:
		target = e.target

	msg = "Test back."
	conn.privmsg(target, msg)