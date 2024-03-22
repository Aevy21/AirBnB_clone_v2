#!/usr/bin/python3
"""
Flask web application with specified routes and template rendering
"""

from flask import Flask, render_template

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
    # Replace underscore symbols (_) with a space
    text_with_spaces = text.replace('_', ' ')
    return f'C {text_with_spaces}'

# Route 4: Display "Python " followed by the value of the text variable
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is_cool'):
    # Replace underscore symbols (_) with a space
    text_with_spaces = text.replace('_', ' ')
    return f'Python {text_with_spaces}'

# Route 5: Display "n is a number" if n is an integer
@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    return f'{n} is a number'

# Route 6: Display HTML page with "Number: n" if n is an integer
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    if isinstance(n, int):
        return render_template('number_template.html', number=n)
    else:
        return 'Not a valid integer'

if __name__ == '__main__':
    # Run the app on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)
