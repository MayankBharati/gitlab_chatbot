
import requests

def make_api_request(url, method='GET', params=None, headers=None):
    """
    Make an API request and return the response.
    
    :param url: The URL to make the request to
    :param method: The HTTP method to use (GET, POST, etc.)
    :param params: Dictionary of query parameters
    :param headers: Dictionary of HTTP headers
    :return: Response object
    """
    try:
        response = requests.request(method, url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def get_gitlab_api_data(endpoint, token):
    """
    Make a request to the GitLab API.
    
    :param endpoint: The API endpoint to request
    :param token: The GitLab API token
    :return: JSON response from the API
    """
    base_url = "https://gitlab.com/api/v4"
    headers = {"Authorization": f"Bearer {token}"}
    return make_api_request(f"{base_url}/{endpoint}", headers=headers)
