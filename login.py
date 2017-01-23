# import Flask class from flask module
from flask import Flask, render_template, redirect, url_for, request , session , flash
from functools import wraps

# application object is then created
app = Flask(__name__)

app.secret_key = "mine"

# login required decorator that stops un logged in users from sending git request to index page
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return  f(*args, **kwargs)
		else:
			flash ('You need to login first.')
			return redirect(url_for('login'))
	return wrap



# Use decorators to link function to url
@app.route('/')
@login_required
def home():
	return render_template('index.html') # render a template



@app.route('/welcome')
def welcome():
	return render_template('welcome.html') # render a template



# Decorator for login
@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid credentials. Please try again.'
		else:
			session['logged_in'] = True
			flash('You were just logged in!')
			return redirect(url_for('home'))
	return render_template('login.html', error = error)



# Logout decorator
@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	flash('You were just logged out!')
	return redirect(url_for('welcome'))



#starting the server with the run method
# debug helps check for errors in the app code and display error messages
if __name__ == '__main__':
	app.run(debug=True)