#!/usr/bin/python3
""" Creating my first flask program
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)
strict_slashes = False


@app.route('/hbnb_filters', strict_slashes=False)
def hbnbFilters():
    """Filters webpage
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def close_db(error):
    """close storage
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
