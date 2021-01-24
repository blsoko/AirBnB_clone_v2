#!/usr/bin/python3
""" Creating my first flask program
"""
from flask import Flask, render_template

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


@app.route('/c/<text>')
def displayText(text):
    """ display “C ” followed by the value
    """
    return ("C %s" % text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def pythonText(text):
    """ display “Python ” followed by the value
    """
    return ("Python %s" % text.replace('_', ' '))


@app.route('/number/<int:n>')
def displayNumber(n):
    """ display “C ” followed by the value
    """
    return ("%d is a number" % n)


@app.route('/number_template/<int:n>')
def displayTemplate(n):
    """ display template html file
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
