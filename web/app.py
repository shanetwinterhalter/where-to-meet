from flask import Flask, render_template, request
from isochrone import main as get_crossover


app = Flask(__name__)

max_time = 60
default_time = 30


def validate_travel_time(travel_time):
    if travel_time > max_time:
        return max_time
    elif travel_time < 1:
        return default_time
    else:
        return travel_time


@app.route("/")
def front_page():
    return render_template('front_page.html', max_time=max_time)


@app.route('/calculate', methods=['GET'])
def calculate_distance():
    if request.method == 'GET':
        args = request.args
        travel_time = validate_travel_time(
                        args.get("travelTime", default=default_time, type=int))
        addresses = zip(args.getlist("address"), args.getlist("transportType"))
        success, locations = get_crossover(travel_time, addresses)
        return render_template('calculate.html', success=success,
                               locations=locations, travel_time=travel_time)
