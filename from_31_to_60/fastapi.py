'''server side sending on the header'''


from fastapi import FastAPI, HTTPException, Header

app = FastAPI()

# Endpoint with header authentication
@app.get("/protected")
async def protected_endpoint(api_key: str = Header(...)):
    # cheak the database for the api key
    # Check the API key
    if api_key != "YOUR_EXPECTED_API_KEY":
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    return {"message": "Access granted"}





import requests

'''client side sending on the header'''
# Base URL of the FastAPI server
base_url = "http://localhost:8000"

# Headers with the API key
headers = {
    "api_key": "YOUR_EXPECTED_API_KEY"
}

# Send the GET request with headers to the FastAPI server
response = requests.get(f"{base_url}/protected", headers=headers)

# Check the response status code
if response.status_code == 200:
    # Successful response
    result = response.json()
    print("Server response:", result)
else:
    # Error response
    print("Error:", response.text)



#########################################################


'''server side sending on the body'''
# if you want some parms or body to de optional use None 
# example: async def create_user(user: User=None):
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Example Pydantic model for the data in the request body
class User(BaseModel):
    username: str
    email: str

# Endpoint to receive and process the data in the request body
@app.post("/create_user")
async def create_user(user: User):
    # Access the data in the request body through the 'user' parameter
    # Perform any necessary operations with the received data
    # For demonstration purposes, let's just return the received user data
    return {"user": user}




'''client side sending on the body'''
import requests

# Base URL of the FastAPI server
base_url = "http://localhost:8000"

# Example data to be sent in the request body
data = {
    "username": "john_doe",
    "email": "john.doe@example.com"
}

# Send the POST request with data in the request body to the FastAPI server
response = requests.post(f"{base_url}/create_user", json=data)

# Check the response status code
if response.status_code == 200:
    # Successful response
    result = response.json()
    print("User created successfully:", result)
else:
    # Error response
    print("Error creating user:", response.text)
