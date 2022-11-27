import traveltimepy as ttpy
from datetime import datetime

# These values don't exist in lat/long
lat_error_value = 181
long_error_value = 181


def location_coords(source_locations):
    geoencoded_locations = []
    success = True
    for item in source_locations:
        if item != "":
            encoded_data = ttpy.geocoding(item)
            if len(encoded_data['features']) > 0:
                geoencoded_locations.append({
                    "source_location": item[0],
                    "travel_method": item[1],
                    "encoding_success": True,
                    "latitude": encoded_data['features'][0][
                        'geometry']['coordinates'][1],
                    "longitude": encoded_data['features'][0][
                        'geometry']['coordinates'][0]
                    })
            else:
                success = False
                geoencoded_locations.append({
                    "source_location": item[0],
                    "travel_method": item[1],
                    "encoding_success": False,
                    "latitude": lat_error_value,
                    "longitude": long_error_value
                })
    return success, geoencoded_locations


def calculate_centre(addresses):
    sum_lat = 0
    sum_lng = 0
    no_addresses = len(addresses)
    for address in addresses:
        sum_lat += float(address['latitude'])
        sum_lng += float(address['longitude'])
    return {
        "latitude": sum_lat/no_addresses,
        "longitude": sum_lng/no_addresses,
        "zoom": 12
    }


def gen_search_data(travel_time, source_coords):
    searches = []
    search_ids = []
    for idx, loc in enumerate(source_coords):
        searches.append({
            'id': str(idx),
            'departure_time':  datetime.utcnow().isoformat(),
            'travel_time': travel_time * 60,
            'coords': {'lat': loc['latitude'], 'lng': loc['longitude']},
            'transportation': {'type': loc['travel_method']},
        })
        search_ids.append(str(idx))
    return searches, search_ids


def generate_intersection(search_ids):
    return {
        'id': "intersection",
        'search_ids': search_ids
    }


def obtain_map_data(searches, intersection):
    return ttpy.time_map(departure_searches=searches,
                         intersections=[intersection])


def extract_intersection_coords(intersection):
    intersect_coords = []
    for shell in intersection['results']:
        if shell['search_id'] == "intersection":
            for shell in shell['shapes']:
                shell_coords = []
                for coord in shell['shell']:
                    shell_coords.append((coord['lat'], coord['lng']))
                intersect_coords.append(shell_coords)
    return intersect_coords


def find_shell_centre(intersect_coords):
    sum_x = 0
    sum_y = 0
    total_points = len(intersect_coords)
    if total_points == 0:
        return (lat_error_value, long_error_value)
    for point in intersect_coords:
        sum_x += point[0]
        sum_y += point[1]
    return (sum_x/total_points, sum_y/total_points)


def find_shell_centres(intersect_coords):
    shell_centres = []
    for item in intersect_coords:
        shell_centres.append(find_shell_centre(item))
    return shell_centres


def location_strings(coords):
    location_strings = []
    for item in coords:
        if item[0] != lat_error_value and item[1] != long_error_value:
            text_location = ttpy.geocoding_reverse(
                item[0], item[1])
            location_strings.append({
                "text_location": text_location[
                                    'features'][0]['properties']['name'],
                "success": True,
                "latitude": item[0],
                "longitude": item[1]
                })
    return location_strings


def main(travel_time, source_locations):
    # Convert locations to lat & long
    success, source_coords = location_coords(source_locations)
    print(source_coords)
    centre = calculate_centre(source_coords)
    if success:
        # Create search json for each location
        searches, search_ids = gen_search_data(travel_time, source_coords)
        # Create intersection json for all searches
        intersect_json = generate_intersection(search_ids)
        # Send API request to obtain data
        intersection = obtain_map_data(searches, intersect_json)
        # Get coordinates of each intersection shell
        intersection_coords = extract_intersection_coords(intersection)
        # Find the centre of each intersection shell
        shell_centres = find_shell_centres(intersection_coords)
        # Return results
        return success, source_coords, location_strings(shell_centres), centre
    else:
        # If fails, return source_coords to help user figure
        # out what they did wrong
        return success, source_coords, [], centre
