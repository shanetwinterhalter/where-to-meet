import app_config
from debug_vars import request as debug_request


def validate_travel_time(hours, mins):
    travel_time = hours * 60 + mins
    if travel_time > app_config.max_time:
        return app_config.max_time
    elif travel_time < 1:
        return app_config.default_time
    else:
        return travel_time


def validate_addresses(address_list, transport_type_list):
    addresses = [
        {
            "address": address,
            "transport_type": transport_type_list[idx]
        }
        for idx, address in enumerate(address_list)
        if (address != "") and transport_type_list[idx]
        in app_config.valid_transport_types]
    return addresses


def validate_request(input_data):
    if app_config.request_debug:
        return debug_request
    travel_time = validate_travel_time(input_data.get("travelTimeHours",
                                       default=0, type=int),
                                       input_data.get("travelTimeMins",
                                       default=0, type=int))
    addresses = validate_addresses(input_data.getlist("address"),
                                   input_data.getlist("transportType"))
    return {
        "travel_time": travel_time,
        "addresses": addresses,
    }
