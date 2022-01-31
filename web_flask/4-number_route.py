#!/usr/bin/python3
'''starting flasf web application'''

from flask import Flask
app = Flask(__name__)


@app.route('/',strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb',strict_slashes=False)
def hi_hbnb():
    return 'HBNB'

@app.route('/c/<text>',strict_slashes=False)
def c_text():
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/')
@app.route('/pyrhon/<text>')
def python(text="is cool"):
    return 'Python {}'.format(text.replace('_', ' '))

@app.route("/number/<int:n>")
def number(n):
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0.', port=5000)
