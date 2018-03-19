#coding=utf-8

import click
from flask import Flask

app = Flask(__name__)

@app.cli.command()
def initdb():
	click.echo('init db')