#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """Closes the current SQLAlchemy Session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states_list():
    """Displays a list of all State objects sorted by name"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)

    return render_template('states_list.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    """Displays dynamic HTML page for URI `/states/<id>`"""
    all_states = storage.all(State).values()
    for state in all_states:
        if id == state.id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

