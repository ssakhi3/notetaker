from flask import Flask, render_template
from dbco import connection as db

app = Flask('MyApp')

@app.route('/')
@app.route('/hello')
@app.route('/hello/<userId>')
def hello(userId=None):
	return render_template('signup.html', userId=userId)


@app.route('/notes/<userId>')
def show_notes(userId=None):
	userId = int(userId)
	x = list(db.notes.find({"userId":userId}))
	print x
	note_titles = ['Chem 1212', 'PHYS 2211', 'CS 1331', 'ENGL 1102']
	if not x:
		x = note_titles

	else:
		x = [note[u'title'] for note in x]
	return render_template('show_notes.html', userId=userId, note_titles=x)	


app.debug = True
app.run()