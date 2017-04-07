from Nexy.db import DB

def run(event, conn):
	plugin_info = parse_plugin_info(event.arguments[0])
	if plugin_info is None:
		send_register_help_message(event, conn)
	else:
		add_filter_to_db(plugin_info['id'], plugin_info['phrase'])

def parse_plugin_info(raw_input):
	raw_input_array = raw_input.split()
	# expected input: nexy !register <plugin_id> <phrase>
	if len(raw_input_array) < 4:
		return None
	
	id = raw_input_array[2]
	phrase = raw_input_array[3]
	return {'id': id, 'phrase': phrase}

def add_filter_to_db(id, phrase):
	db = DB()
	doc = {'id': '{}'.format(id), 'phrase': '{}'.format(phrase)}
	db.add_filter(doc)

def send_register_help_message(e, conn):
	msg_type = e.type
	if msg_type == "privmsg":
		target = e.source.nick
	else:
		target = e.target

	help_msg = "Register a plugin: nexy !register <plugin_id> <trigger_phrase>"
	conn.privmsg(target, help_msg)