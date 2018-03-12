#coding=utf-8

from flask import request
from flask import Flask,url_for

app = Flask(__name__)

@app.route('/')
def index():
	return 'index page'
	# user_agent = request.headers.get('User-Agent')
	# return '<p>Browser is %s</p>' %user_agent

@app.route('/hello/')
def hello():
	return 'hello world'

@app.route('/user/<username>')
def show_user_profile(username):
	return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return 'post %d' % post_id

@app.route('/projects/')
def projects():
	return 'the project page'

@app.route('/about')
def about():
	return 'the about page'

with app.test_request_context():
	print url_for('hello')
	print url_for('projects')
	# print url_for('login',next='/')
	# print url_for('profle',username='Jone')

if __name__ == '__main__':
	app.run()