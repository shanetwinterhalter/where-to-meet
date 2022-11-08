import traveltimepy as ttpy
import os
from datetime import datetime

os.environ["TRAVELTIME_ID"] = '9e92dc47'
os.environ["TRAVELTIME_KEY"] = 'ea73781a50a84f6135b7a46ec5b3d03a'


def location_coords(source_locations):
    geoencoded_locations = []
    for item in source_locations:
        geoencoded_locations.append(
            ttpy.geocoding(item)['features'][0]['geometry']['coordinates'])
    return geoencoded_locations


def gen_search_data(travel_time, source_coords):
    searches = []
    search_ids = []
    for idx, loc in enumerate(source_coords):
        searches.append({
            'id': str(idx),
            'departure_time':  datetime.utcnow().isoformat(),
            'travel_time': travel_time * 60,
            'coords': {'lat': loc[1], 'lng': loc[0]},
            'transportation': {'type': "public_transport"},
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


def find_intersection(travel_time, source_locations):
    source_coords = location_coords(source_locations)
    searches, search_ids = gen_search_data(travel_time, source_coords)
    intersection = generate_intersection(search_ids)
    return obtain_map_data(searches, intersection)


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
        return (-1, -1)
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
        if item[0] != -1 and item[1] != -1:
            location_strings.append({
                "text_location": ttpy.geocoding_reverse(
                    item[0], item[1])['features'][0]['properties']['name'],
                "latitude": item[0],
                "longitude": item[1]
                })
        else:
            print("Error - no intersection found")
            location_strings.append({
                "text_location": "No intersection found",
                "latitude": item[0],
                "longitude": item[1]
            })
    return location_strings


def main(travel_time, source_locations):
    intersection = find_intersection(travel_time, source_locations)
    intersection_coords = extract_intersection_coords(intersection)
    shell_centres = find_shell_centres(intersection_coords)
    return location_strings(shell_centres)
