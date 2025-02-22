import json
import boto3

comprehend = boto3.client("comprehend")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("TwitterSentimentAnalysis")

def lambda_handler(event, context):
    for record in event['Records']:
        tweet = json.loads(record["body"])
        sentiment = comprehend.detect_sentiment(Text=tweet["text"], LanguageCode="en")["Sentiment"]
        
        table.put_item(
            Item={"tweet_id": tweet["tweet_id"], "text": tweet["text"], "user": tweet["user"], "sentiment": sentiment}
        )

    return {"statusCode": 200, "body": "Sentiment analysis complete"}
