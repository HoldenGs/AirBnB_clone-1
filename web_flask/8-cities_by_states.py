#!/usr/bin/python3

from os import getenv
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/cities_by_states')
def cities_by_states():
    states = sorted(storage.all('State').values(),
                    key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


"""
    states = []
    for state in state_list:
        states.append([state, sorted(state.cities, key=lambda c: c.name)])
"""


@app.teardown_appcontext
def close_session(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
