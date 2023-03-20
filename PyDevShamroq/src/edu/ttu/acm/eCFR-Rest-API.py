import requests

# Set the API endpoint and the parameters for the request
eCFR_BASE_URL_V1 = "https://www.ecfr.gov/api/versioner/v1/"
ANCESTRY = "/ancestry/2020-01-01/"
PARAMS = "title-16.json?chapter=I&subchapter=C&part=312&section=312.5 -H accept: application/json"


def getStatus():
    url = eCFR_BASE_URL_V1 + ANCESTRY + PARAMS
    params = {"param1": "value1", "param2": "value2"}
    # Make a GET request to the API and store the response
    response = requests.get(url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the response content
        print(response.content)
    else:
        # Print an error message
        print("Error: API request failed with status code", response.status_code)
