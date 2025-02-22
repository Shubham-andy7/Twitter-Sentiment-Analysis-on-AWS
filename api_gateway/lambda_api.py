import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("TwitterSentimentAnalysis")

def lambda_handler(event, context):
    tweet_id = event["queryStringParameters"]["tweet_id"]
    response = table.get_item(Key={"tweet_id": tweet_id})
    
    return {"statusCode": 200, "body": json.dumps(response["Item"])}
