import requests

response = requests.get("https://abc123.execute-api.us-east-1.amazonaws.com/prod/sentiment?tweet_id=12345")
print(response.json())
