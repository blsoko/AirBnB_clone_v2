#!/usr/bin/python3
""" Creating my first flask program
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
strict_slashes = False
app.jinja_env.add_extension('jinja2.ext.do')


@app.route('/states')
@app.route('/states/<id>')
def states_db(id=0):
    """ display cities by state
    """
    states = storage.all(State)
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def close_db(error):
    """close storage
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
