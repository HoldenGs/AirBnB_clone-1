#!/usr/bin/python3

from os import getenv
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/cities_by_states')
def cities_by_states():
    if getenv('HBNB_TYPE_STORAGE', None) == 'db':
        states = sorted(storage.all('State').values(),
                        key=lambda state: state.name)
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
