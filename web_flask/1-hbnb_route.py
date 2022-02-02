#!/usr/bin/python3
'''starting flasf web application'''

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''to display'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hi_hbnb():
    '''an other one'''
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
