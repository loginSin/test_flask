#coding=utf-8


def get_db():
	if not hasattr(g,'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
	if hasattr(g,'sqlite_db'):
		g.sqlite_db.close()