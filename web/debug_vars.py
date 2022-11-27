# Request Data

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

# Response Data

debug_locations = [
    {
        'text_location': 'Premier Goldberg, Canal Wharf, Canal Wharf '
        'Industrial Estate, Wexham, Slough, Buckinghamshire, England, '
        'SL3 6EG, United Kingdom',
        'success': True,
        'latitude': 51.50905373214288,
        'longitude': -0.5408464724999998
    },
    {
        'text_location': 'Slough Bus Station, Brunel Way, Slough, '
        'England, SL1 1FQ, United Kingdom',
        'success': True,
        'latitude': 51.51103561176474,
        'longitude': -0.5927810454117648
    },
]
centre = {
        "latitude": 51.50323,
        "longitude": -0.56,
        "zoom": 14
}
travel_time = 45

response = {
        "travel_time": travel_time,
        "locations": debug_locations,
        "map_centre": centre,
        "success": True
    }
