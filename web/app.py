from flask import Flask, render_template, request
from isochrone import main as get_crossover


app = Flask(__name__)

max_time = 60
default_time = 30


@app.route("/")
def front_page():
    return render_template('front_page.html', max_time=max_time)


@app.route('/calculate', methods=['GET'])
def calculate_distance():
    if request.method == 'GET':
        args = request.args
        travel_time = args.get("travelTime", default=20, type=int)
        addresses = args.getlist("address")
        if travel_time > max_time:
            travel_time = max_time
        elif travel_time < 1:
            travel_time = default_time
        success, locations = get_crossover(travel_time, addresses)
        print(success)
        print(locations)
        return render_template('calculate.html', success=success,
                               locations=locations, travel_time=travel_time)
