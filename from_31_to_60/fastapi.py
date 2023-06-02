'''server side'''


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

'''client side'''
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
