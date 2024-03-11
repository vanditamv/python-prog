# Python program for API testing with authentication, for authentication and performing authenticated requests:
import requests

def authenticate(username, password):
    auth_url = 'https://example.com/authenticate'
    credentials = {'username': username, 'password': password}
    response = requests.post(auth_url, json=credentials)
    if response.status_code == 200:
        token = response.json().get('token')
        return token
    else:
        print("Authentication failed.")
        return None

def perform_authenticated_request(url, token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def main():
    username = 'your_username'
    password = 'your_password'
    api_url = 'https://example.com/api/resource'

    # Authenticate and obtain token
    token = authenticate(username, password)
    if token:
        # Perform authenticated request
        response_data = perform_authenticated_request(api_url, token)
        if response_data:
            print("Response:", response_data)

if __name__ == "__main__":
    main()
