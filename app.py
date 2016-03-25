from flask import Flask, render_template
from dbco import connection as db
from note import Note

app = Flask('MyApp')

@app.route('/')
@app.route('/index')
@app.route('/hello')
@app.route('/hello/<userId>')
@app.route('/hello/<userId>/<note_titles>')
def hello(userId=None, content = None):
	return render_template('signup.html', userId=userId, content=content)

#if note id, find single note
# if no note id, find all notes
#if multiple note ids, show all
@app.route('/notes/<noteId>')
@app.route('/notes/')
def show_notes(noteId=None):
	#note_titles = ['Chem 1212', 'PHYS 2211', 'CS 1331', 'ENGL 1102']
	#content= ["Enter content here"]
	if noteId:
		note = (list(db.notes.find({'noteId': noteId})))[0]
		note_title = note.get('title')
		content = note.get('content')
	else:
		notesJson = list(db.notes.find({}))
		notes = map(Note.from_json, notesJson)
		note_titles = []
		contents = []
		noteIds = []
		for note in notes: 
			note_titles.append(note.title)
			contents.append(note.content)
			noteIds.append(note.noteId)


	return render_template('show_notes.html', titles=note_titles, noteIds=noteIds)	


app.debug = True
app.run()