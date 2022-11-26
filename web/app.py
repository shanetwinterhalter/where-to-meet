import traveltimepy as ttpy
import app_config

from flask import Flask, render_template, redirect, request, url_for
from isochrone import main as get_crossover
from utils import validate_travel_time, validate_addresses

app = Flask(__name__)

debug = True


@app.route("/", methods=['GET', 'POST'])
def front_page():
    if request.method == 'POST':
        submit_error = request.args['submit_error']
    else:
        submit_error = False
    return render_template('front_page.html',
                           max_time=app_config.max_time,
                           submit_error=submit_error)


@app.route('/calculate', methods=['POST'])
def calculate_distance():
    if debug:
        import debug_vars as debug_vars
        return render_template('calculate.html',
                               success=debug_vars.success,
                               locations=debug_vars.debug_locations,
                               centre=debug_vars.centre,
                               travel_time=debug_vars.travel_time)
    args = request.values
    # Default time is validated later, so just set to any int for now
    travel_time = validate_travel_time(
        args.get("travelTime", default=0, type=int))
    valid, addresses = validate_addresses(args.getlist("address"),
                                          args.getlist("transportType"))
    if valid:
        success, locations, centre = get_crossover(travel_time, addresses)
        return render_template('calculate.html',
                               success=success,
                               locations=locations,
                               centre=centre,
                               travel_time=travel_time)
    else:
        return redirect(url_for('.front_page', code=307, submit_error=True))


@app.route('/autocomplete', methods=['GET'])
def autofill_address():
    return ttpy.geocoding(request.args.get("query"))
