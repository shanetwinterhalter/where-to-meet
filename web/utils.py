import app_config


def validate_travel_time(travel_time):
    if travel_time > app_config.max_time:
        return app_config.max_time
    elif travel_time < 1:
        return app_config.default_time
    else:
        return travel_time


def validate_addresses(address_list, transport_type_list):
    addresses = [(address, transport_type_list[idx])
                 for idx, address in enumerate(address_list)
                 if address != ""]
    input_success = True if len(addresses) > 0 else False
    return input_success, addresses
