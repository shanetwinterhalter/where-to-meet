from travel_time import location_coords, calculate_centre, calculate_results
from app_config import response_debug, maps_api_key, tt_app_id, tt_api_key
from debug_vars import response as debug_response
from traveltimepy.sdk import TravelTimeSdk


def generate_response(request_data):
    if response_debug:
        return debug_response
    travel_time = request_data['travel_time']
    sdk = TravelTimeSdk(tt_app_id, tt_api_key)
    source_coords, error_addresses = location_coords(sdk,
                                                     request_data['addresses'])
    map_centre = calculate_centre(source_coords)
    locations = calculate_results(sdk, travel_time, source_coords)
    return {
        "travel_time": travel_time,
        "source_addresses": source_coords,
        "error_addresses": error_addresses,
        "map_centre": map_centre,
        "result_locations": locations,
        "maps_api_key": maps_api_key
    }
