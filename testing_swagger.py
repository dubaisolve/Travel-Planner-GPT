import requests

# Base URL of your Flask app
base_url = "https://tripy.azurewebsites.net/" #http://localhost https://api.li8re.com/ tripy.azurewebsites.net

# Test data for each endpoint
test_data = {
    'location_search': {
        'url': f"{base_url}/location/search",
        'params': {'key': 'your_api_key_for_trip_adv', 'searchQuery': 'Rome'}
    },
    'location_reviews': {
        'url': f"{base_url}/location/187791/reviews",
        'params': {'key': 'your_api_key_for_trip_adv', 'language': 'en'}
    },
    'location_photos': {
        'url': f"{base_url}/location/187791/photos",
        'params': {'key': 'your_api_key_for_trip_adv', 'language': 'en'}
    },
    'location_details': {
        'url': f"{base_url}/location/187791/details",
        'params': {'key': 'your_api_key_for_trip_adv', 'language': 'en', 'currency': 'USD'}
    },
    'nearby_search': {
        'url': f"{base_url}/location/nearby_search",
        'params': {'latLong': '42.3455,-71.10767', 'key': 'your_api_key_for_trip_adv', 'language': 'en'}
    }
}

def test_endpoint(endpoint_name):
    endpoint = test_data[endpoint_name]
    response = requests.get(endpoint['url'], params=endpoint['params'])
    print(f"Testing {endpoint_name}:")
    print("URL:", response.url)
    print("Status Code:", response.status_code)
    print("Response:", response.json())
    print("\n" + "-"*50 + "\n")

# Testing each endpoint
for endpoint in test_data:
    test_endpoint(endpoint)
