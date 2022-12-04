import traveltimepy as ttpy
from datetime import datetime


def _gen_search_data(travel_time, source_coords):
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


def _generate_intersection(search_ids):
    return {
        'id': "intersection",
        'search_ids': search_ids
    }


def _obtain_map_data(searches, intersection):
    return ttpy.time_map(departure_searches=searches,
                         intersections=[intersection])


def _extract_intersection_coords(intersection):
    intersect_coords = []
    for shell in intersection['results']:
        if shell['search_id'] == "intersection":
            for shell in shell['shapes']:
                shell_coords = []
                for coord in shell['shell']:
                    shell_coords.append((coord['lat'], coord['lng']))
                intersect_coords.append(shell_coords)
    return intersect_coords


def _find_shell_centre(intersect_coords):
    sum_x = 0
    sum_y = 0
    total_points = len(intersect_coords)
    for point in intersect_coords:
        sum_x += point[0]
        sum_y += point[1]
    return (sum_x/total_points, sum_y/total_points)


def _get_location_string(lat, lng):
    return ttpy.geocoding_reverse(lat, lng)['features'][0][
        'properties']['label']


def _format_shell_coords(shell):
    shell_coords = []
    for coord in shell:
        shell_coords.append({
            "lat": coord[0],
            "lng": coord[1]
        })
    return shell_coords


def _parse_map_data(intersection_data):
    results = []
    intersection_coords = _extract_intersection_coords(intersection_data)
    if intersection_coords == [[]]:
        return []
    for shell in intersection_coords:
        centre_lat, centre_lng = _find_shell_centre(shell)
        centre_location = _get_location_string(centre_lat, centre_lng)
        shell_coords = _format_shell_coords(shell)
        results.append({
            "centre_location": centre_location,
            "centre_latitude": centre_lat,
            "centre_longitude": centre_lng,
            "shell_edges": shell_coords
        })
    return results


def calculate_results(travel_time, source_coords):
    if len(source_coords) == 0:
        return {}
    # Create search json for each location
    searches, search_ids = _gen_search_data(travel_time, source_coords)
    # Create intersection json for all searches
    intersect_json = _generate_intersection(search_ids)
    # Send API request to obtain data
    intersection_data = _obtain_map_data(searches, intersect_json)
    # Parse map data & return
    return _parse_map_data(intersection_data)


def location_coords(source_locations):
    geoencoded_locations = []
    geoencoding_failed_locations = []
    for item in source_locations:
        if item != "":
            encoded_data = ttpy.geocoding(item['address'])
            if len(encoded_data['features']) > 0:
                geoencoded_locations.append({
                    "source_location": item['address'],
                    "travel_method": item['transport_type'],
                    "latitude": encoded_data['features'][0][
                        'geometry']['coordinates'][1],
                    "longitude": encoded_data['features'][0][
                        'geometry']['coordinates'][0]
                    })
            else:
                geoencoding_failed_locations.append({
                    "source_location": item['address'],
                    "travel_method": item['transport_type']
                })
    return geoencoded_locations, geoencoding_failed_locations


def calculate_centre(addresses):
    if len(addresses) == 0:
        return {}
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
