provider "aws" {
  region = "us-east-1"
}

resource "aws_kinesis_stream" "twitter_stream" {
  name        = "TwitterStream"
  shard_count = 1
}

resource "aws_dynamodb_table" "twitter_sentiment" {
  name           = "TwitterSentimentAnalysis"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "tweet_id"

  attribute {
    name = "tweet_id"
    type = "S"
  }
}

output "kinesis_stream_name" {
  value = aws_kinesis_stream.twitter_stream.name
}
