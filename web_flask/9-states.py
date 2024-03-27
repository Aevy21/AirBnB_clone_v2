#!/usr/bin/python3
"""
Starts a Flask web application
"""


from flask import Flask, render_template, abort
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
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('states_list.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    """Displays dynamic HTML page for URI `/states/<id>`"""
    state = storage.get(State, id)
    if state is None:
        return render_template("not_found.html")
    
    if storage.__class__.__name__ == 'DBStorage':
        cities = sorted(state.cities, key=lambda city: city.name)
    else:
        cities = sorted(state.cities(), key=lambda city: city.name)
    
    return render_template("state_cities.html", state=state, cities=cities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
