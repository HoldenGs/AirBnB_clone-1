#!/usr/bin/python3

from os import getenv
from models import storage
from flask import Flask, render_template
app = Flask(__name__)

"""
        states = []
        for c, s in storage.__session.query(City, State).join(State).order_by(City.name):
            if s not in states:
                states.append(s)
            else:
                states[states.index(s)].cities.append(c)
"""

@app.route('/cities_by_states')
def cities_by_states():
    if getenv('HBNB_TYPE_STORAGE', None) == 'db':
        states = sorted(storage.all('State').values(),
                        key=lambda state: state.name)
        cities = sorted(storage.all('City').values(),
                        key=lambda city: city.name)
        for city in cities:
            for state in states:
                if city.state_id == state.id:
                    state.cities.append(city)
    else:
        states = sorted(storage.all('State').values(),
                        key=lambda state: state.name)
        cities = sorted(storage.all('City').values(),
                        key=lambda city: city.name)
        for city in cities:
            for state in states:
                if city.state_id == state.id:
                    state.cities.append(city)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close_session(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
