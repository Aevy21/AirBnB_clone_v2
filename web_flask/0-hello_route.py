#!/usr/bin/python3
"""
Simple Flask web application
"""

from flask import Flask

app = Flask(__name__)

# Route to display "Hello HBNB!"
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route function to return Hello HBNB"""
    return "Hello HBNB!"

if __name__ == "__main__":
    # Run the app on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
