import boto3

client = boto3.client("kinesis", region_name="us-east-1")

response = client.create_stream(
    StreamName="TwitterStream",
    ShardCount=1
)

print("Kinesis Stream Created:", response)
