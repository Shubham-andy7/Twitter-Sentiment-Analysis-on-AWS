import json
import boto3
import tweepy

kinesis_client = boto3.client("kinesis", region_name="us-east-1")

auth = tweepy.OAuthHandler("API_KEY", "API_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_SECRET")
api = tweepy.API(auth)

def lambda_handler(event, context):
    tweets = api.search_tweets(q="AWS", lang="en", count=10)
    for tweet in tweets:
        tweet_data = {"tweet_id": tweet.id, "text": tweet.text, "user": tweet.user.screen_name}
        kinesis_client.put_record(
            StreamName="TwitterStream", 
            Data=json.dumps(tweet_data), 
            PartitionKey="default"
        )

    return {"statusCode": 200, "body": "Tweets sent to Kinesis"}
