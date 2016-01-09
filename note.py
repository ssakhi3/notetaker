from datetime import datetime as dt

class Note(object):

	def __init__(self, title, content,  userId, date_created=dt.now(), date_modified=dt.now(), noteId=None):
		
		if not all([title, content, userId]):
			raise ValueError

		self.title = title
		self.content = content
		self.userId = userId
		self.noteId = noteId

		self.date_created = date_created
		self.date_modified = date_modified

	def create_json(self): 
		mynote = dict()
		mynote["title"] = sef.title
		mynote["content"] = self.content
		mynote["userId"] = self.userId
		mynote["noteId"] = self.noteId

		mynote["date_created"] = self.date_created
		mynote["date_modified"] = self.date_modified

		return mynote

	@classmethod
	def read_json(constructor, mynote):
		title = mynote.get("title")
		content = mynote.get("content")
		userId = mynote.get("userId")
		noteId = mynote.get("noteId")

		date_created = mynote.get("date_created")
		date_modified = mynote.get("date_modified")

		return constructor(title, content,  userId, date_created, date_modified, noteId)

	def update_time(self):
		self.date_modified = dt.now()