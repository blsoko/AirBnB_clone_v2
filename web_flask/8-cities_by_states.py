#!/usr/bin/python3
""" Creating my first flask program
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
strict_slashes = False


@app.route('/cities_by_states')
def get_db():
    """ display cities by state
    """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close_db(error):
    """close storage
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
