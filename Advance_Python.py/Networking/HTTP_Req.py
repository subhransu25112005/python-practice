'''POST /login HTTP/1.1
Host: example.com
Content-Type: application/json

{
  "username": "john",
  "password": "1234"
}
'''
'''import requests

url = "https://example.com/login"
payload = {
    "username": "john",
    "password": "1234"
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print("Status Code:", response.status_code)
print("Response Body:", response.text)'''

import requests

def login_example():
    # Target URL (a test API endpoint)
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Data we want to send (like login credentials)
    payload = {
        "username": "john",
        "password": "1234"
    }
    
    # Headers to tell the server we’re sending JSON
    headers = {
        "Content-Type": "application/json"
    }
    
    # Send POST request
    response = requests.post(url, json=payload, headers=headers)
    
    # Print results
    print("Status Code:", response.status_code)
    print("Response Headers:", response.headers)
    print("Response Body:", response.json())

if __name__ == "__main__":
    login_example()