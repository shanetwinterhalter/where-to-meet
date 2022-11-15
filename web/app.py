import traveltimepy as ttpy
import app_config

from flask import Flask, render_template, redirect, request, url_for
from isochrone import main as get_crossover
from utils import validate_travel_time, validate_addresses

app = Flask(__name__)


@app.route("/")
def front_page():
    try:
        submit_error = request.args['submit_error']
    except ValueError:
        submit_error = False
    return render_template('front_page.html',
                           max_time=app_config.max_time,
                           submit_error=submit_error)


@app.route('/calculate', methods=['GET'])
def calculate_distance():
    if request.method == 'GET':
        args = request.args
        # Default time is validated later, so just set to any int for now
        travel_time = validate_travel_time(
                        args.get("travelTime", default=0, type=int))
        valid, addresses = validate_addresses(args.getlist("address"),
                                              args.getlist("transportType"))
        if valid:
            success, locations = get_crossover(travel_time, addresses)
            return render_template('calculate.html',
                                   success=success,
                                   locations=locations,
                                   travel_time=travel_time)
        else:
            return redirect(url_for('.front_page', submit_error=True))


@app.route('/autocomplete', methods=['GET'])
def autofill_address():
    return ttpy.geocoding(request.args.get("query"))
