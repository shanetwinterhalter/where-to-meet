from os import getenv

# API key for Google Maps
maps_api_key = getenv('GMAPS_API_KEY')

# This is determined by the TravelTime API
max_time = 60
# The value to use when the user doesn't enter a time
default_time = 30

# Whether to use the debug request data
request_debug = True
# Whether to use debug response data
response_debug = True

# List of supported transport methods
valid_transport_types = ["public_transport", "driving", "cycling", "walking"]
