from isochrone import main as calculate_results
from app_config import response_debug
from debug_vars import response as debug_response


def generate_response(request_data):
    if response_debug:
        return debug_response
    success, source_coords, locations, map_centre = calculate_results(
        request_data['travel_time'], request_data['addresses'])
    return {
        "travel_time": request_data['travel_time'],
        "source_addresses": source_coords,
        "locations": locations,
        "map_centre": map_centre,
        "source_coords_found": success
    }
