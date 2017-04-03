from pymongo import MongoClient
import re
import logging
import traceback

class DB:
	def __init__(self, h='', p=27017):
		#TODO: put this in config file
		self.h = h
		self.p = p
		self.db_name = "nexy"
		self.log = logging.getLogger('nexy.db')
		self.client = self.connect()
		self.log.info('Database ready to go')
		
	def connect(self):
		# TODO: db.auth(<user>, <pass>)
		self.log.debug('Connecting to mongo...')
		try:
			if self.h is '':
				self.log.debug('Host is empty, creating client using default "localhost"')
				self.client = MongoClient(port=self.p)
			else:
				self.log.debug('Host is {}, creating client'.format(self.h))
				self.client = MongoClient(host=self.h, port=self.p)
			self.log.debug('Connected to database')
			return self.client[self.db_name]
		except Exception as e:
			self.log.error('Error while trying to connect to database {}'.format(e))
			self.log.error('{}'.format(traceback.format_exc()))
	def add_filter(self, json):
		#TODO: Add checks here for json errors (valid syntax + required fields)
		self.insert_one(json, 'filter')
		
	def find(self, query, collection):
		c = self.client[collection].find(query)
		if c.count() is 0:
			c = None
		return c

	def update (self, oldquery, newquery, collection, options=None):
		return self.client[collection].update(oldquery,newquery)

	def findAll(self, collection):
		"""
		Query db
		"""
		try:
			return self.client[collection].find()
		except:
			self.log.error('Could not findAll() with collection: {}'.format(collection))
			self.log.error(traceback.format_exc())
	def insert_one(self, doc, collection):
		"""
		Insert one document into <collection> based on <doc>
		"""
		if collection is None:
			self.log.error('Collection is empty, cannot insert on doc: {}'.format(doc))
			pass
		else:
			try:
				return self.client[collection].insert_one(doc)
			except:
				self.log.error('Could not insert into collection {} with doc {}'.format(collection, doc))
				self.log.error(traceback.format_exc())
	def insert_many(self, docs, collection):
		"""
		Insert multiple documents into <collection>
		"""
		if collection is None:
			self.log.error('Collection is empty, cannot insert documents')
		else:
			try:
				return self.client[collection].insert_many(docs)
			except:
				self.log.error('Could not insert documents into collection {}'.format(collection))
				self.log.error(traceback.format_exc())
	def remove(self, query, collection):
		"""
		Remove document(s) from <collection> based on <query>
		"""
		if collection is None:
			self.log.error('Collection is empty, cannot insert documents')
		else:
			try:
				return self.client[collection].remove(query)
			except:
				self.log.error('Could not remove document(s) from collection: {} with query: {}'.format(collection, query))
				self.log.error(traceback.format_exc())
