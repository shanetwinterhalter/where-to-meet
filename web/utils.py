import app_config


def validate_travel_time(travel_time):
    if travel_time > app_config.max_time:
        return app_config.max_time
    elif travel_time < 1:
        return app_config.default_time
    else:
        return travel_time
