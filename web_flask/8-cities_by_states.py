#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
       the list of all State objects present in DBStorage
    """
    state_obj = storage.all(State)
    state_dict = []
    for k, v in state_obj.items():
        state_dict.append(v)
    return render_template('7-states_list.html', state_dict=state_dict)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    """
       display the states and cities listed in alphabetical order
    """
    state_obj = storage.all(State)
    state_dict = []
    for k, v in state_obj.items():
        state_dict.append(v)
    return render_template('8-cities_by_states.html', state_dict=state_dict)


@app.teardown_appcontext
def teardown_db(exception):
    """
       closes the storage on teardown
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
