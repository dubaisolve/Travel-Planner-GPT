from flask import Flask, request, jsonify
import requests
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Set the hardcoded API key
TRIPADVISOR_API_KEY = "your_trip_adv_api_key"

@app.route('/location/search', methods=['GET'])
def location_search():
    logging.info('Handling location search request.')
    required_params = ['searchQuery']
    optional_params = ['category', 'phone', 'address', 'latLong', 'radius', 'radiusUnit', 'language']
    params = {param: request.args.get(param) for param in required_params + optional_params if request.args.get(param)}
    params['key'] = TRIPADVISOR_API_KEY  # Add the hardcoded API key to the params
    if not all(params.get(param) for param in required_params):
        return jsonify({"message": "Missing required query parameters"}), 400
    url = 'https://api.content.tripadvisor.com/api/v1/location/search'
    response = requests.get(url, params=params, headers={'accept': 'application/json'})
    return jsonify(response.json()), response.status_code

@app.route('/location/<locationId>/reviews', methods=['GET'])
def location_reviews(locationId):
    logging.info(f'Handling reviews request for location ID: {locationId}')
    params = {'key': TRIPADVISOR_API_KEY, 'language': request.args.get('language')}
    url = f'https://api.content.tripadvisor.com/api/v1/location/{locationId}/reviews'
    response = requests.get(url, params=params, headers={'accept': 'application/json'})
    return jsonify(response.json()), response.status_code

@app.route('/location/<locationId>/photos', methods=['GET'])
def location_photos(locationId):
    logging.info(f'Fetching photos for location ID: {locationId}')
    params = {'key': TRIPADVISOR_API_KEY}
    if request.args.get('language'):
        params['language'] = request.args.get('language')
    url = f'https://api.content.tripadvisor.com/api/v1/location/{locationId}/photos'
    response = requests.get(url, params=params, headers={'accept': 'application/json'})
    return jsonify(response.json()), response.status_code

@app.route('/location/<locationId>/details', methods=['GET'])
def location_details(locationId):
    logging.info(f'Fetching details for location ID: {locationId}')
    params = {'key': TRIPADVISOR_API_KEY}
    if request.args.get('language'):
        params['language'] = request.args.get('language')
    if request.args.get('currency'):
        params['currency'] = request.args.get('currency')
    url = f'https://api.content.tripadvisor.com/api/v1/location/{locationId}/details'
    response = requests.get(url, params=params, headers={'accept': 'application/json'})
    return jsonify(response.json()), response.status_code

@app.route('/location/nearby_search', methods=['GET'])
def nearby_search():
    logging.info('Handling nearby location search request.')
    required_params = ['latLong']
    optional_params = ['category', 'phone', 'address', 'radius', 'radiusUnit', 'language']
    params = {param: request.args.get(param) for param in required_params + optional_params if request.args.get(param)}
    params['key'] = TRIPADVISOR_API_KEY  # Add the hardcoded API key to the params
    if not all(params.get(param) for param in required_params):
        return jsonify({"message": "Missing required query parameters"}), 400
    url = 'https://api.content.tripadvisor.com/api/v1/location/nearby_search'
    response = requests.get(url, params=params, headers={'accept': 'application/json'})
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
