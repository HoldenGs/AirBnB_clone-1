#!/usr/bin/python3

from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states', defaults={'id': None}, strict_slashes=False)
@app.route('/states/<id>')
def state_cities(id):
    states = sorted(storage.all('State').values(),
                    key=lambda state: state.name)
    if id is None:
        route = 'states'
    else:
        states_list = states
        states = None
        for state in states_list:
            if state.id == id:
                route = 'state_cities'
                return render_template('9-states.html',
                                       states=state, route=route)
        if states is None:
            route = 'none_found'
    return render_template('9-states.html',
                           states=states, route=route)


@app.teardown_appcontext
def close_session(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
