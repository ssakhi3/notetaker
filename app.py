from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('signup.html', name=name)


@app.route('/notes/<username>')
def show_notes(username=None):
	note_titles = ['Chem 1212', 'PHYS 2211', 'CS 1331', 'ENGL 1102']
	return render_template('show_notes.html', username=username, note_titles=note_titles)	


app.debug = True
app.run()