# Import module for HTTP requests and function for basic authentication
import requests
from requests.auth import HTTPBasicAuth

# URL, the authentication endpoint
url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

# Default credentials for Cisco DevNet Sandbox
username = "devnetuser"
password = "Cisco123!"

# Make variable saving the response from the server
response = requests.post(url, auth=HTTPBasicAuth(username, password))

# Checking the response for status code
if response.status_code == 200:
    token = response.json()["Token"]
    print(f"Token: {token}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)