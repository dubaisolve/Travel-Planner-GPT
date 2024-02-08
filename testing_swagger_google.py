import requests

def test_google_maps_api():
    api_key = 'your_gg_api_key_'  # Replace with your actual API key
    url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants%20in%20Sydney&key={api_key}'
    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # This will print the JSON response
    else:
        return f'Error: {response.status_code}'

# Run the function
print(test_google_maps_api())
