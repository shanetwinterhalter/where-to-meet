# Where-to-meet

This is a web app that allows a user to input a number of addresses (up to 10) and a travel time and calculates good places for all those people to meet. 

It is currently running at https://where-to-meet.herokuapp.com/

# JSON Request Schema

This is the JSON schema of the reques that is passed to the TravelTime API functions. This doesn't quite match what comes from the client, but the client information is converted into this.

```
{
    "travel_time": 20,
    "addresses": [
        {
            "address": "London Paddington station, Praed Street, Paddington, London, Greater London, England, W2 1HQ, United Kingdom",
            "transport_type": "public_transport"
        },
        {
            "address": "Trafalgar Square, Seven Dials, Covent Garden, City of Westminster, Greater London, England, WC2N 5DS, United Kingdom",
            "transport_type": "cycling"
        }
    ]
}
```

# JSON Response Schema

This is the JSON response schema from the server to the client.

```
{
    "travel_time": 20,
    "source_addresses": [
        {
            'source_location': 'London Paddington station, Praed Street, Paddington, London, Greater London, England, W2 1HQ, United Kingdom',
            'travel_method': 'public_transport',
            'latitude': 51.5169294,
            'longitude': -0.1773378
        },
        {
            'source_location': 'Trafalgar Square, Seven Dials, Covent Garden, City of Westminster, Greater London, England, WC2N 5DS, United Kingdom',
            'travel_method': 'cycling',
            'latitude': 51.508037,
            'longitude': -0.1280494
        }
    ],
    "error_addresses": [
        {
            'source_location': 'Trafalgar Square, Seven Dials, Covent Garden, City of Westminster, Greater London, England, WC2N 5DS, United Kingdom',
            'travel_method': 'cycling'
        },
        {
            'source_location': 'London Paddington station, Praed Street, Paddington, London, Greater London, England, W2 1HQ, United Kingdom',
            'travel_method': 'public_transport',
        }
    ]
    "map_centre": {
        "latitude": 51.50323,
        "longitude": -0.56
    },
    "result_locations": [
        {
            "centre_location": "East End Cosmetics, Middlesex Street, Bishopsgate, City of London, Greater London, England, E1 7JJ, United Kingdom",
            "centre_latitude": 51.51797828000001,
            "centre_longitude": -0.07903208167999999,
            "shell_edges": [
                {
                    "latitude": 51.51709,
                    "longitude": -0.07344485
                },
                {
                    "latitude": 51.517963,
                    "longitude": -0.07483859
                },
                {
                    "latitude": 51.51886,
                    "longitude": -0.07483859
                },
                {
                    "latitude": 51.51931,
                    "longitude": -0.0755582
                }
            ]
        },
        {
            "centre_location": "Westminster City Council - Lisson Grove, 215, Lisson Grove, St. John's Wood, London, Greater London, England, NW8 8LF, United Kingdom",
            "centre_latitude": 51.525971999999996,
            "centre_longitude": -0.17205012,
            "shell_edges": [
                {
                    "latitude": 51.526253,
                    "longitude": -0.17238112
                },
                {
                    "latitude": 51.52605,
                    "longitude": -0.17270446
                },
                {
                    "latitude": 51.52522,
                    "longitude": -0.17137133
                },
                {
                    "latitude": 51.525803,
                    "longitude": -0.17137133
                }
            ]
        }
    ],
    "maps_api_key": "Google Maps API key"
}
```
