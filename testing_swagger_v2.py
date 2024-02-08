import requests

# Base URL of your Flask app
base_url = "https://tripy.azurewebsites.net/" # Choose the correct URL for your app

# Test data for each endpoint
test_data = {
    'location_search': {
        'url': f"{base_url}/location/search",
        'params': {'searchQuery': 'La Farine Café & Bakery'}
    },
    'location_reviews': {
        'url': f"{base_url}/location/187791/reviews",
        'params': {'language': 'en'}
    },
    'location_photos': {
        'url': f"{base_url}/location/187791/photos",
        'params': {'language': 'en'}
    },
    'location_details': {
        'url': f"{base_url}/location/187791/details",
        'params': {'language': 'en', 'currency': 'USD'}
    },
    'nearby_search': {
        'url': f"{base_url}/location/nearby_search",
        'params': {'latLong': '42.3455,-71.10767', 'language': 'en'}
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
