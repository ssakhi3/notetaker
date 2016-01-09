

class Note(object):

	def __init__(self, title, date_created, date_modified,  content,  userId,  noteId= None):
		if not all([title, content, userId]):
			raise ValueError


		self.title = title
		self.date_created = date_created
		self.date_modified = date_modified
		self.content = content
		self.userId = userId
		self.noteId = noteId

	def create_json(self): 
		mynote = dict()
		mynote["title"] = sef.title
		mynote["date_created"] = self.date_created
		mynote["date_modified"] = self.date_modified
		mynote["content"] = self.content
		mynote["userId"] = self.userId
		mynote["noteId"] = self.noteId

		return mynote

	@classmethod
	def read_json(constructor, mynote):
		title = mynote.get("title")
		date_created = mynote.get("date_created")
		date_modified = mynote.get("date_modified")
		content = mynote.get("content")
		userId = mynote.get("userId")
		noteId = mynote.get("noteId")

		return constructor(title, date_created, date_modified, content, userId, noteId)