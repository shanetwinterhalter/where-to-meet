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
            {'latitude': 51.507126, 'longitude': -0.19573171},
            {'latitude': 51.507553, 'longitude': -0.19504757},
            {'latitude': 51.507553, 'longitude': -0.1936081},
            {'latitude': 51.508003, 'longitude': -0.19288838},
            {'latitude': 51.508904, 'longitude': -0.19288838},
            {'latitude': 51.5098, 'longitude': -0.19144891},
            {'latitude': 51.51025, 'longitude': -0.19216864},
            {'latitude': 51.51025, 'longitude': -0.19429252},
            {'latitude': 51.509872, 'longitude': -0.19429252},
            {'latitude': 51.508972, 'longitude': -0.19573171},
            {'latitude': 51.507126, 'longitude': -0.19573171}
        ]
    },
    {
        'centre_location': '27, Pembridge Square, Notting Hill, Royal Borough '
        'of Kensington and Chelsea, London, Greater London, England, W2 4TB, '
        'United Kingdom',
        'centre_latitude': 51.511840400000004,
        'centre_longitude': -0.19541265000000002,
        'shell_edges': [
            {'latitude': 51.511646, 'longitude': -0.19569272},
            {'latitude': 51.51212, 'longitude': -0.19493398},
            {'latitude': 51.51212, 'longitude': -0.19501212},
            {'latitude': 51.51167, 'longitude': -0.19573171},
            {'latitude': 51.511646, 'longitude': -0.19569272}
        ]
    },
    {
        'centre_location': '118, George Street, Marylebone, London, Greater '
        'London, England, W1H 5RL, United Kingdom',
        'centre_latitude': 51.51643420192307,
        'centre_longitude': -0.16151673490384616,
        'shell_edges': [
            {'latitude': 51.512547, 'longitude': -0.19144891},
            {'latitude': 51.5116, 'longitude': -0.19144891},
            {'latitude': 51.5098, 'longitude': -0.18856998},
            {'latitude': 51.508904, 'longitude': -0.18856998},
            {'latitude': 51.508453, 'longitude': -0.18785024},
            {'latitude': 51.51025, 'longitude': -0.18497132},
            {'latitude': 51.509354, 'longitude': -0.18353185},
            {'latitude': 51.509354, 'longitude': -0.18065292},
            {'latitude': 51.508453, 'longitude': -0.17921345},
            {'latitude': 51.509354, 'longitude': -0.17777398},
            {'latitude': 51.509354, 'longitude': -0.17633452},
            {'latitude': 51.51025, 'longitude': -0.17489505},
            {'latitude': 51.51025, 'longitude': -0.1691372},
            {'latitude': 51.51205, 'longitude': -0.16625826},
            {'latitude': 51.51205, 'longitude': -0.1648188},
            {'latitude': 51.5107, 'longitude': -0.1626596},
            {'latitude': 51.5098, 'longitude': -0.1626596},
            {'latitude': 51.509354, 'longitude': -0.16193986},
            {'latitude': 51.509354, 'longitude': -0.16050039},
            {'latitude': 51.508453, 'longitude': -0.15906094},
            {'latitude': 51.508453, 'longitude': -0.15762147},
            {'latitude': 51.506657, 'longitude': -0.15474254},
            {'latitude': 51.506657, 'longitude': -0.15330307},
            {'latitude': 51.505756, 'longitude': -0.1518636},
            {'latitude': 51.505756, 'longitude': -0.14610575},
            {'latitude': 51.506657, 'longitude': -0.14466628},
            {'latitude': 51.506657, 'longitude': -0.14178735},
            {'latitude': 51.508003, 'longitude': -0.13962816},
            {'latitude': 51.508904, 'longitude': -0.13962816},
            {'latitude': 51.509354, 'longitude': -0.13890842},
            {'latitude': 51.509354, 'longitude': -0.13459001},
            {'latitude': 51.508453, 'longitude': -0.13315056},
            {'latitude': 51.508453, 'longitude': -0.12883216},
            {'latitude': 51.509354, 'longitude': -0.1273927},
            {'latitude': 51.509354, 'longitude': -0.12595323},
            {'latitude': 51.5107, 'longitude': -0.12379403},
            {'latitude': 51.5116, 'longitude': -0.12379403},
            {'latitude': 51.512497, 'longitude': -0.12235457},
            {'latitude': 51.51699, 'longitude': -0.12235457},
            {'latitude': 51.51789, 'longitude': -0.1209151},
            {'latitude': 51.51879, 'longitude': -0.1209151},
            {'latitude': 51.520138, 'longitude': -0.1230743},
            {'latitude': 51.520138, 'longitude': -0.1273927},
            {'latitude': 51.521038, 'longitude': -0.12883216},
            {'latitude': 51.521038, 'longitude': -0.1317111},
            {'latitude': 51.522835, 'longitude': -0.13459001},
            {'latitude': 51.522835, 'longitude': -0.13602948},
            {'latitude': 51.521935, 'longitude': -0.13746895},
            {'latitude': 51.521935, 'longitude': -0.13890842},
            {'latitude': 51.52149, 'longitude': -0.13962816},
            {'latitude': 51.520588, 'longitude': -0.13962816},
            {'latitude': 51.519688, 'longitude': -0.14106761},
            {'latitude': 51.51879, 'longitude': -0.14106761},
            {'latitude': 51.51834, 'longitude': -0.14178735},
            {'latitude': 51.519238, 'longitude': -0.14322682},
            {'latitude': 51.519238, 'longitude': -0.14466628},
            {'latitude': 51.520138, 'longitude': -0.14610575},
            {'latitude': 51.520138, 'longitude': -0.1475452},
            {'latitude': 51.521935, 'longitude': -0.15042414},
            {'latitude': 51.521935, 'longitude': -0.15330307},
            {'latitude': 51.521038, 'longitude': -0.15474254},
            {'latitude': 51.52149, 'longitude': -0.15546227},
            {'latitude': 51.523285, 'longitude': -0.15546227},
            {'latitude': 51.523735, 'longitude': -0.156182},
            {'latitude': 51.523735, 'longitude': -0.15906094},
            {'latitude': 51.522835, 'longitude': -0.16050039},
            {'latitude': 51.523735, 'longitude': -0.16193986},
            {'latitude': 51.523735, 'longitude': -0.1648188},
            {'latitude': 51.522835, 'longitude': -0.16625826},
            {'latitude': 51.522835, 'longitude': -0.16769773},
            {'latitude': 51.523285, 'longitude': -0.16841745},
            {'latitude': 51.52418, 'longitude': -0.16841745},
            {'latitude': 51.52463, 'longitude': -0.1691372},
            {'latitude': 51.523735, 'longitude': -0.17057666},
            {'latitude': 51.524704, 'longitude': -0.17212974},
            {'latitude': 51.524704, 'longitude': -0.17342407},
            {'latitude': 51.524254, 'longitude': -0.17414366},
            {'latitude': 51.523354, 'longitude': -0.17414366},
            {'latitude': 51.522007, 'longitude': -0.17630246},
            {'latitude': 51.522907, 'longitude': -0.17774168},
            {'latitude': 51.522907, 'longitude': -0.17918088},
            {'latitude': 51.522007, 'longitude': -0.18062007},
            {'latitude': 51.521557, 'longitude': -0.18151958},
            {'latitude': 51.521557, 'longitude': -0.18259898},
            {'latitude': 51.522007, 'longitude': -0.18349849},
            {'latitude': 51.522007, 'longitude': -0.18493769},
            {'latitude': 51.521557, 'longitude': -0.1856573},
            {'latitude': 51.52066, 'longitude': -0.1856573},
            {'latitude': 51.52021, 'longitude': -0.18493769},
            {'latitude': 51.52021, 'longitude': -0.18349849},
            {'latitude': 51.51976, 'longitude': -0.18277888},
            {'latitude': 51.51931, 'longitude': -0.18349849},
            {'latitude': 51.51931, 'longitude': -0.18493769},
            {'latitude': 51.51886, 'longitude': -0.1856573},
            {'latitude': 51.517963, 'longitude': -0.1856573},
            {'latitude': 51.517513, 'longitude': -0.1863769},
            {'latitude': 51.517513, 'longitude': -0.1878161},
            {'latitude': 51.517063, 'longitude': -0.1885357},
            {'latitude': 51.514366, 'longitude': -0.1885357},
            {'latitude': 51.513916, 'longitude': -0.1892553},
            {'latitude': 51.513916, 'longitude': -0.19069451},
            {'latitude': 51.51347, 'longitude': -0.1914141},
            {'latitude': 51.51257, 'longitude': -0.1914141},
            {'latitude': 51.512547, 'longitude': -0.19144891}
        ]
    }
]

response = {
        "travel_time": travel_time,
        "source_addresses": source_addresses,
        "error_addresses": error_addresses,
        "map_centre": map_centre,
        "result_locations": result_locations,
    }
