import requests

# URL for the Google Places Photo API
base_url = "https://maps.googleapis.com/maps/api/place/photo"

# Parameters for the API request
params = {
    "maxwidth": 400,
    "photo_reference": "AWU5eFja8Ah5nDLfoty1Y0yRmXOUp35kmYrPrEEX6sW6kj7PRSA3WVpHvjFujQY1ll-LDmShzlDHL2IfZMawHpNR6X96GuCLHq-KGDpGpq6J1b0Eqx7rI03RoMlAgnCc5hZCE0OkNSxTq-Yzk50C5JngoWIwTmZ4szcIcsi2pGWLVlgGqXQC",
    "key": "your_gg_api_key_"
}

# Prepare the full URL (for demonstration purposes)
prepared_url = requests.Request('GET', base_url, params=params).prepare().url
print("Prepared URL (Image URL):", prepared_url)

# Send the GET request
response = requests.get(prepared_url, stream=True)

# Check if the request was successful
if response.status_code == 200:
    # Display the type of data received
    print("Response Content-Type:", response.headers['Content-Type'])
    print("Image data retrieved successfully.")
else:
    print("Error:", response.status_code)
