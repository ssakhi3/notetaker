from flask import Flask, render_template

app = Flask(__userId__)

@app.route('/')
@app.route('/hello')
@app.route('/hello/<userId>')
def hello(userId=None):
	return render_template('signup.html', userId=userId)


@app.route('/notes/<userId>')
def show_notes(userId=None):
	note_titles = ['Chem 1212', 'PHYS 2211', 'CS 1331', 'ENGL 1102']
	return render_template('show_notes.html', username=username, note_titles=note_titles)	


app.debug = True
app.run()