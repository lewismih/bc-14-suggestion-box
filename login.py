# import Flask class from flask module
from flask import Flask, render_template

# application object is then created
app = Flask(__name__)


# Use decorators to link function to url
@app.route('/')
def home():
	return 'Home'

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin ' or request.form['password'] != 'admin':
			error = 'Invalid credentials. Please Try again.'
		else:
			return redirect(url_for('home'))
	return render_template('login.html', error = error)

#starting the server with the run method
# debug helps check for errors in the app code and display error messages
if __name__ == '__main__':
	app.run(debug=True)