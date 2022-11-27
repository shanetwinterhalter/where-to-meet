# Example Request Data

request = {
        "travel_time": 20,
        "addresses": [
            ('London Paddington station, Praed Street, Paddington, London,'
             'Greater London, England, W2 1HQ, United Kingdom',
             'public_transport'),
            ('Trafalgar Square, Seven Dials, Covent Garden, City of '
             'Westminster, Greater London, England, WC2N 5DS, United Kingdom',
             'public_transport')
        ],
        "valid_input": True
    }

# Example Response Data

debug_locations = [
    {
        'text_location': 'Premier Goldberg, Canal Wharf, Canal Wharf '
        'Industrial Estate, Wexham, Slough, Buckinghamshire, England, '
        'SL3 6EG, United Kingdom',
        'encoding_success': True,
        'latitude': 51.50905373214288,
        'longitude': -0.5408464724999998
    },
    {
        'text_location': 'Slough Bus Station, Brunel Way, Slough, '
        'England, SL1 1FQ, United Kingdom',
        'encoding_success': True,
        'latitude': 51.51103561176474,
        'longitude': -0.5927810454117648
    },
]
source_coords = [
    {
        'source_location': 'London Paddington station, Praed Street,'
        ' Paddington, London, Greater London, England, W2 1HQ, United Kingdom',
        'travel_method': 'public_transport',
        'encoding_success': True,
        'latitude': 51.5169294,
        'longitude': -0.1773378
    },
    {
        'source_location': 'Trafalgar Square, Seven Dials, Covent Garden, '
        'City of Westminster, Greater London, England, WC2N 5DS, United '
        'Kingdom',
        'travel_method': 'public_transport',
        'encoding_success': True,
        'latitude': 51.508037,
        'longitude': -0.1280494
    }
]
centre = {
        "latitude": 51.50323,
        "longitude": -0.56,
        "zoom": 14
}
travel_time = 45

response = {
        "travel_time": travel_time,
        "source_addresses": source_coords,
        "locations": debug_locations,
        "map_centre": centre,
        "source_coords_found": True
    }
