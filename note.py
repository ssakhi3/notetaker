from dbco import db
from datetime import datetime as dt
import random

class Note(object):

	def __init__(self, title, content,  userId=1234, date_created=dt.now(), date_modified=dt.now(), noteId=None):
		
		if not all([title, content, userId]):
			raise ValueError

		if noteId is None:
			foundDuplicate = True
			while foundDuplicate:
				randomInt = random.randint(5000,100000)
				if (db.notes.find_one({'noteId':randomInt}) is None):
					foundDuplicate = False
			noteId = randomInt
			print noteId
		self.title = str(title)
		self.content = str(content)
		self.userId = int(userId)
		self.noteId = int(noteId)

		self.date_created = date_created
		self.date_modified = date_modified

	def to_json(self): 
		mynote = dict()
		mynote["title"] = self.title
		mynote["content"] = self.content
		mynote["userId"] = self.userId
		mynote["noteId"] = self.noteId

		mynote["date_created"] = self.date_created
		mynote["date_modified"] = self.date_modified

		return mynote

	@classmethod
	def from_json(constructor, mynote):
		title = mynote.get("title")
		content = mynote.get("content")
		userId = mynote.get("userId")
		noteId = mynote.get("noteId")

		date_created = mynote.get("date_created")
		date_modified = mynote.get("date_modified")

		return constructor(title, content,  userId, date_created, date_modified, noteId)

	def update_time(self):
		self.date_modified = dt.now()