import traveltimepy as ttpy
import app_config

from flask import Flask, render_template, redirect, request, url_for
from request import validate_request
from response import generate_response

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def front_page():
    if request.method == 'POST':
        submit_error = True
    else:
        submit_error = False
    return render_template('front_page.html',
                           max_time=app_config.max_time,
                           submit_error=submit_error)


@app.route('/calculate', methods=['POST'])
def calculate_distance():
    request_data = validate_request(request.values)
    if len(request_data['addresses']) > 0:
        response_data = generate_response(request_data)
        return render_template('calculate.html',
                               response_data=response_data)
    else:
        return redirect(url_for('.front_page'), code=307)


@app.route('/autocomplete', methods=['GET'])
def autofill_address():
    return ttpy.geocoding(request.args.get("query"))
