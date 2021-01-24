#!/usr/bin/python3
""" Creating my first flask program
"""
from flask import Flask

app = Flask(__name__)
strict_slashes = False


@app.route('/')
def hello():
    """ Display hello hbnb at host='0.0.0.0', port=5000
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hellohbtn():
    """ Display HBTN
    """
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
