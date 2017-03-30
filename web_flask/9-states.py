#!/usr/bin/python3

from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states')
def states():
    states = sorted(storage.all('State').values(),
                    key=lambda state: state.name)
    route = 'states'
    return render_template('9-states.html',
                           states=states, route=route)


@app.route('/states/<string:id>')
def state_cities(id):
    states_list = storage.all('State').values()
    states = None
    for state in states_list:
        if state.id == id:
            states = state
    if states:
        route = 'state_cities'
    else:
        route = 'none_found'
    return render_template('9-states.html',
                           states=states, route=route)


@app.teardown_appcontext
def close_session(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
