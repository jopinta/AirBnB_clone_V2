#!/usr/bin/python3
'''starting flasf web application'''

from flask import Flask
app = Flask(__name__)
app.url_map.srict_slashes = False


@app.route('/')
def hello_hbnb():
    '''to display'''
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host='0.0.0.0.', port=5000, debug=True)
