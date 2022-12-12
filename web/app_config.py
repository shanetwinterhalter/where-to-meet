from os import getenv

# API key for Google Maps
maps_api_key = getenv('GMAPS_API_KEY')

# Traveltime API keys
tt_api_key = getenv('TRAVELTIME_KEY')
tt_app_id = getenv('TRAVELTIME_ID')

# This is determined by the TravelTime API
max_time = 60
# The value to use when the user doesn't enter a time
default_time = 30

# Whether to use the debug request data
request_debug = False
# Whether to use debug response data
response_debug = False

# List of supported transport methods
valid_transport_types = ["public_transport", "driving", "cycling", "walking"]
