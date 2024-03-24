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
def state_cities(id):
    """Displays cities linked to a State"""
    state = storage.get(State, id)
    if state:
        cities = state.cities if hasattr(state, 'cities') else state.cities()
        sorted_cities = sorted(cities, key=lambda x: x.name)
        return render_template('state_cities.html', state=state, cities=sorted_cities)
    else:
        return render_template('not_found.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

