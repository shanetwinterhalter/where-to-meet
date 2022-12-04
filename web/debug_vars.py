from app_config import maps_api_key

# Example Request Data

request = {
    'travel_time': 20,
    'addresses': [
        {
            'address': 'London Paddington station, Praed Street, Paddington, '
            'London, Greater London, England, W2 1HQ, United Kingdom',
            'transport_type': 'public_transport'
        },
        {
            'address': 'Trafalgar Square, Seven Dials, Covent Garden, City of '
            'Westminster, Greater London, England, WC2N 5DS, United Kingdom',
            'transport_type': 'cycling'
        }
    ]
}

# Example Response Data
travel_time = 20
source_addresses = [
    {
        'source_location': 'London Paddington station, Praed Street, '
        'Paddington, London, Greater London, England, W2 1HQ, United Kingdom',
        'travel_method': 'public_transport',
        'latitude': 51.5169294,
        'longitude': -0.1773378
    },
    {
        'source_location': 'Trafalgar Square, Seven Dials, Covent Garden, City'
        ' of Westminster, Greater London, England, WC2N 5DS, United Kingdom',
        'travel_method': 'cycling',
        'latitude': 51.508037,
        'longitude': -0.1280494
    }
]
error_addresses = []
map_centre = {
    'latitude': 51.512483200000005,
    'longitude': -0.15269359999999998,
    'zoom': 12
}
result_locations = [
    {
        'centre_location': 'Mall Chambers, Palace Gardens Terrace, Notting '
        'Hill, Royal Borough of Kensington and Chelsea, London, Greater '
        'London, England, W8 4AT, United Kingdom',
        'centre_latitude': 51.508673545454535,
        'centre_longitude': -0.1939845590909091,
        'shell_edges': [
            {'lat': 51.507126, 'lng': -0.19573171},
            {'lat': 51.507553, 'lng': -0.19504757},
            {'lat': 51.507553, 'lng': -0.1936081},
            {'lat': 51.508003, 'lng': -0.19288838},
            {'lat': 51.508904, 'lng': -0.19288838},
            {'lat': 51.5098, 'lng': -0.19144891},
            {'lat': 51.51025, 'lng': -0.19216864},
            {'lat': 51.51025, 'lng': -0.19429252},
            {'lat': 51.509872, 'lng': -0.19429252},
            {'lat': 51.508972, 'lng': -0.19573171},
            {'lat': 51.507126, 'lng': -0.19573171}
        ]
    },
    {
        'centre_location': '27, Pembridge Square, Notting Hill, Royal Borough '
        'of Kensington and Chelsea, London, Greater London, England, W2 4TB, '
        'United Kingdom',
        'centre_latitude': 51.511840400000004,
        'centre_longitude': -0.19541265000000002,
        'shell_edges': [
            {'lat': 51.511646, 'lng': -0.19569272},
            {'lat': 51.51212, 'lng': -0.19493398},
            {'lat': 51.51212, 'lng': -0.19501212},
            {'lat': 51.51167, 'lng': -0.19573171},
            {'lat': 51.511646, 'lng': -0.19569272}
        ]
    },
    {
        'centre_location': '118, George Street, Marylebone, London, Greater '
        'London, England, W1H 5RL, United Kingdom',
        'centre_latitude': 51.51643420192307,
        'centre_longitude': -0.16151673490384616,
        'shell_edges': [
            {'lat': 51.512547, 'lng': -0.19144891},
            {'lat': 51.5116, 'lng': -0.19144891},
            {'lat': 51.5098, 'lng': -0.18856998},
            {'lat': 51.508904, 'lng': -0.18856998},
            {'lat': 51.508453, 'lng': -0.18785024},
            {'lat': 51.51025, 'lng': -0.18497132},
            {'lat': 51.509354, 'lng': -0.18353185},
            {'lat': 51.509354, 'lng': -0.18065292},
            {'lat': 51.508453, 'lng': -0.17921345},
            {'lat': 51.509354, 'lng': -0.17777398},
            {'lat': 51.509354, 'lng': -0.17633452},
            {'lat': 51.51025, 'lng': -0.17489505},
            {'lat': 51.51025, 'lng': -0.1691372},
            {'lat': 51.51205, 'lng': -0.16625826},
            {'lat': 51.51205, 'lng': -0.1648188},
            {'lat': 51.5107, 'lng': -0.1626596},
            {'lat': 51.5098, 'lng': -0.1626596},
            {'lat': 51.509354, 'lng': -0.16193986},
            {'lat': 51.509354, 'lng': -0.16050039},
            {'lat': 51.508453, 'lng': -0.15906094},
            {'lat': 51.508453, 'lng': -0.15762147},
            {'lat': 51.506657, 'lng': -0.15474254},
            {'lat': 51.506657, 'lng': -0.15330307},
            {'lat': 51.505756, 'lng': -0.1518636},
            {'lat': 51.505756, 'lng': -0.14610575},
            {'lat': 51.506657, 'lng': -0.14466628},
            {'lat': 51.506657, 'lng': -0.14178735},
            {'lat': 51.508003, 'lng': -0.13962816},
            {'lat': 51.508904, 'lng': -0.13962816},
            {'lat': 51.509354, 'lng': -0.13890842},
            {'lat': 51.509354, 'lng': -0.13459001},
            {'lat': 51.508453, 'lng': -0.13315056},
            {'lat': 51.508453, 'lng': -0.12883216},
            {'lat': 51.509354, 'lng': -0.1273927},
            {'lat': 51.509354, 'lng': -0.12595323},
            {'lat': 51.5107, 'lng': -0.12379403},
            {'lat': 51.5116, 'lng': -0.12379403},
            {'lat': 51.512497, 'lng': -0.12235457},
            {'lat': 51.51699, 'lng': -0.12235457},
            {'lat': 51.51789, 'lng': -0.1209151},
            {'lat': 51.51879, 'lng': -0.1209151},
            {'lat': 51.520138, 'lng': -0.1230743},
            {'lat': 51.520138, 'lng': -0.1273927},
            {'lat': 51.521038, 'lng': -0.12883216},
            {'lat': 51.521038, 'lng': -0.1317111},
            {'lat': 51.522835, 'lng': -0.13459001},
            {'lat': 51.522835, 'lng': -0.13602948},
            {'lat': 51.521935, 'lng': -0.13746895},
            {'lat': 51.521935, 'lng': -0.13890842},
            {'lat': 51.52149, 'lng': -0.13962816},
            {'lat': 51.520588, 'lng': -0.13962816},
            {'lat': 51.519688, 'lng': -0.14106761},
            {'lat': 51.51879, 'lng': -0.14106761},
            {'lat': 51.51834, 'lng': -0.14178735},
            {'lat': 51.519238, 'lng': -0.14322682},
            {'lat': 51.519238, 'lng': -0.14466628},
            {'lat': 51.520138, 'lng': -0.14610575},
            {'lat': 51.520138, 'lng': -0.1475452},
            {'lat': 51.521935, 'lng': -0.15042414},
            {'lat': 51.521935, 'lng': -0.15330307},
            {'lat': 51.521038, 'lng': -0.15474254},
            {'lat': 51.52149, 'lng': -0.15546227},
            {'lat': 51.523285, 'lng': -0.15546227},
            {'lat': 51.523735, 'lng': -0.156182},
            {'lat': 51.523735, 'lng': -0.15906094},
            {'lat': 51.522835, 'lng': -0.16050039},
            {'lat': 51.523735, 'lng': -0.16193986},
            {'lat': 51.523735, 'lng': -0.1648188},
            {'lat': 51.522835, 'lng': -0.16625826},
            {'lat': 51.522835, 'lng': -0.16769773},
            {'lat': 51.523285, 'lng': -0.16841745},
            {'lat': 51.52418, 'lng': -0.16841745},
            {'lat': 51.52463, 'lng': -0.1691372},
            {'lat': 51.523735, 'lng': -0.17057666},
            {'lat': 51.524704, 'lng': -0.17212974},
            {'lat': 51.524704, 'lng': -0.17342407},
            {'lat': 51.524254, 'lng': -0.17414366},
            {'lat': 51.523354, 'lng': -0.17414366},
            {'lat': 51.522007, 'lng': -0.17630246},
            {'lat': 51.522907, 'lng': -0.17774168},
            {'lat': 51.522907, 'lng': -0.17918088},
            {'lat': 51.522007, 'lng': -0.18062007},
            {'lat': 51.521557, 'lng': -0.18151958},
            {'lat': 51.521557, 'lng': -0.18259898},
            {'lat': 51.522007, 'lng': -0.18349849},
            {'lat': 51.522007, 'lng': -0.18493769},
            {'lat': 51.521557, 'lng': -0.1856573},
            {'lat': 51.52066, 'lng': -0.1856573},
            {'lat': 51.52021, 'lng': -0.18493769},
            {'lat': 51.52021, 'lng': -0.18349849},
            {'lat': 51.51976, 'lng': -0.18277888},
            {'lat': 51.51931, 'lng': -0.18349849},
            {'lat': 51.51931, 'lng': -0.18493769},
            {'lat': 51.51886, 'lng': -0.1856573},
            {'lat': 51.517963, 'lng': -0.1856573},
            {'lat': 51.517513, 'lng': -0.1863769},
            {'lat': 51.517513, 'lng': -0.1878161},
            {'lat': 51.517063, 'lng': -0.1885357},
            {'lat': 51.514366, 'lng': -0.1885357},
            {'lat': 51.513916, 'lng': -0.1892553},
            {'lat': 51.513916, 'lng': -0.19069451},
            {'lat': 51.51347, 'lng': -0.1914141},
            {'lat': 51.51257, 'lng': -0.1914141},
            {'lat': 51.512547, 'lng': -0.19144891}
        ]
    }
]

response = {
        "travel_time": travel_time,
        "source_addresses": source_addresses,
        "error_addresses": error_addresses,
        "map_centre": map_centre,
        "result_locations": result_locations,
        "maps_api_key": maps_api_key
    }
