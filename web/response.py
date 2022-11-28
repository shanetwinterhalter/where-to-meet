from travel_time import location_coords, calculate_centre, calculate_results
from app_config import response_debug
from debug_vars import response as debug_response


def generate_response(request_data):
    if response_debug:
        return debug_response
    travel_time = request_data['travel_time']
    source_coords, error_addresses = location_coords(request_data['addresses'])
    map_centre = calculate_centre(source_coords)
    locations = calculate_results(travel_time, source_coords)
    return {
        "travel_time": travel_time,
        "source_addresses": source_coords,
        "error_addresses": error_addresses,
        "map_centre": map_centre,
        "result_locations": locations
    }
