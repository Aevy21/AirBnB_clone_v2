#!/usr/bin/python3
"""
Flask web application with specified routes
"""
from flask import Flask
from werkzeug.utils import escape


# Create a Flask app instance
app = Flask(__name__)

# Route 1: Display "Hello HBNB!"


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

# Route 2: Display "HBNB"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

# Route 3: Display "C " followed by the value of the text variable


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    text_with_spaces = text.replace('_', ' ')
    return f'C {escape(text_with_spaces)}'

# Route 4: Display "Python " followed by the value of the text variable


@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is_cool'):
    text_with_spaces = text.replace('_', ' ')
    return f'Python {escape(text_with_spaces)}'

# Route 5: Display "n is a number" if n is an integer


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    return f'{n} is a number'


if __name__ == '__main__':
    # Run the app on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)
