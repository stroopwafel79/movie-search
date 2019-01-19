"""Flask server to run my app on"""
from jinja2 import StrictUndefined

from flask import (Flask, render_template, redirect, request, flash,
                   session, url_for, jsonify)
from flask_sqlalchemy import SQLAlchemy

# This is the connection to the PostgreSQL database; we're getting
# this through the Flask-SQLAlchemy helper library. On this, we can find
# the "session" object, where we do most of our interactions (committing, etc.)

db = SQLAlchemy()


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "12345"

# Normally, if you use an indefined variable in Jinja2, it fails
# silently. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def show_homepage():
    """ Show the homepage"""

    return render_template("homepage.html")


def connect_to_db(app):
	"""Connect the database to our Flask app"""

	# Configure to use our PostgreSQL database
	app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///test"
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
	db.app = app
	db.init_app(app)

######################################################################
if __name__ == '__main__':
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    # Use the DebugToolbar
    #DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')

    # As a convenience, if we run this module interactiverly, it will leave
	# you in a state of being able to work with the database directly.
	import os
	from server import app

	# Connect the Flask app to the database
	connect_to_db(app)

	# Will print when run interactively
	print("Connected to DB")

	# Make tables
	db.create_all()
