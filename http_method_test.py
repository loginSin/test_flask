#coding=utf-8

from flask import request
from flask import Flask
from flask import abort,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
	return redirect(url_for('test'))

@app.route('/test/')
def test():
	abort(401)

@app.route('/login/' , methods=['GET' , 'POST'])
def login():
	if request.method == 'POST':
		print request.form['name']
		print request.args;
		return do_the_login()
	else:
		return show_the_login_form()


def do_the_login():
	return 'do login'

def show_the_login_form():
	return 'show login'


if __name__ == '__main__':
	app.run()