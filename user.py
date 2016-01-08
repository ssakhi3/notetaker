
from datetime import datetime

class User(object):

	def __init__(self, fname, lname, email, password, userid=None):
		
		if not all([fname, lname, email, password]):
			raise ValueError

		self.fname = fname
		self.lname = lname
		self.email = email
		self.password = password

		# TODO: If userid is None, generate one
		self.userid = userid


	def create_json(self):
		myuser = dict()
		myuser['fname'] = self.fname
		myuser['lname'] = self.lname
		myuser['email'] = self.email
		myuser['password'] = self.password
		myuser['userid'] = self.userid

		return myuser


	@classmethod
	def read_json(constructor, myuser):
		fname = myuser.get('fname')
		lname = myuser.get('lname')
		email = myuser.get('email')
		password = myuser.get('password')
		userid = myuser.get('userid')

		return constructor(fname, lname, email, password, userid)

