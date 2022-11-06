from flask import Flask, render_template, request
from isochrone import main as get_crossover


app = Flask(__name__)


@app.route("/")
def front_page():
    return render_template('front_page.html')


@app.route('/calculate', methods=['GET'])
def calculate_distance():
    if request.method == 'GET':
        args = request.args
        travel_time = args.get("travelTime", default=20, type=int)
        addresses = args.getlist("address")
        locations = get_crossover(travel_time, addresses)
        return render_template('calculate.html', locations=locations)
