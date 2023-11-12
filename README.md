# API Tests - Using Python 

## What is Python and Pytest Framework 

`Python` is a high-level, general-purpose programming language known for its simplicity and readability. It was created by Guido van Rossum and first released in 1991. Python is designed to be easy to learn and has a clean and concise syntax, which makes it a popular choice for both beginners and experienced programmers.

The `pytest` framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

### Setup of dependencies for the tests 

```bash
pip install requests
```

```bash
pip install pytest
```

### Definition of the API that will be tested

For this tutorial, we'll use the Nasa API that return a list of asteroids: [Asteroids - NeoWs](https://api.nasa.gov/#donkiGST) and we will test the endpoint that Retrieve a list of Asteroids based on their closest approach date to Earth.

About the API:
- Base URL: `https://api.nasa.gov/neo/rest/v1/feed`
- Query parameters:

| Parameter | Type |Default |Description |
| ---------|---------|--------|-------------------|
|start_date|YYYY-MM-DD|none|Starting date for asteroid search|
|end_date|YYYY-MM-DD|7 days after start_date|Ending date for asteroid search|
|api_key|string|DEMO_KEY|api.nasa.gov key for expanded usage|


For this tutorial, we will focus on three types of tests:
- Contract: If the API is able to validate the query parameters that are sent 
- Status: If the status codes are correct 
- Authentication: Even this API doesn't requires the token, we can do tests with this 

Our Scenarios:

|  Method | Test | Expected Result |
| ---------|--------|-------------------|
| GET | Search with success | - Return a status code 200<br/> The body response contains the list of asteroids|
| GET | Search without any query parameter | - Return a status code 403<br/>|
| GET | Search with start date only|  - Return a status code 200 <br/> The body response contain the list of asteroid|
| GET | Search with end date only|  - Return a status code 200 <br/> The body response contain the list of asteroid|
| GET | Search in an valid range of dates| - Return a status code 200<br/> - The body response contain all fields non empty|
| GET | Search when start date is bigger than end date| - Return a status code 400 <br/>|
| GET | Search with invalid API Token| - Return a status code 403 <br/> The body response contain the list of asteroid|

For more details, check my article [here](https://dev.to/m4rri4nne/automating-your-api-tests-using-python-and-pytest-23cc)
