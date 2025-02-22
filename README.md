# 🐦 Twitter Sentiment Analysis on AWS 🚀  

## **📌 Overview**
This project builds a **real-time Twitter sentiment analysis pipeline** using **AWS services**. It collects tweets, processes them, analyzes sentiment, and visualizes the data using AWS QuickSight.

---

## **📂 Project Architecture**
1️⃣ Data Ingestion
- Fetches tweets using the Twitter API.
- Streams tweets to AWS Kinesis.
  
2️⃣ Data Processing
- AWS Glue ETL processes raw tweets.
- Cleans and stores data in Amazon S3.
  
3️⃣ Sentiment Analysis
- AWS Lambda + Amazon Comprehend analyze tweet sentiment.
- Results stored in DynamoDB.
  
4️⃣ Data Visualization
- AWS Athena + QuickSight create real-time dashboards.
  
5️⃣ REST API
- AWS API Gateway + Lambda provide a public API for sentiment lookup.

---

## **🚀 AWS Services Used**
- **AWS Kinesis** → Real-time tweet ingestion.
- **AWS S3** → Store raw & processed tweet data.
- **AWS Glue** → ETL for data processing.
- **Amazon Comprehend** → Sentiment analysis.
- **AWS DynamoDB** → Store sentiment results.
- **AWS Lambda** → Serverless processing.
- **AWS API Gateway** → Expose REST API.
- **AWS Athena + QuickSight** → Dashboard for insights.

---

## **📜 Setup Guide**
### **🔹 Step 1: Clone the Repo**
```bash
git clone https://github.com/yourusername/twitter-sentiment-analysis-aws.git
cd twitter-sentiment-analysis-aws
```

### **🔹 Step 2: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **🔹 Step 3: Set Up AWS Credentials**
```bash
aws configure
```

### **🔹 Step 4: Deploy AWS Infrastructure (Optional)**
You can use Terraform to deploy AWS resources automatically.
```bash
cd infrastructure
terraform init
terraform apply
```

---

## **📝 Code Breakdown**
### **1️⃣ Data Ingestion (Streaming Tweets to Kinesis)**
📄 data_ingestion/lambda_producer.py
```python
import boto3
import json
import tweepy

# Set up AWS Kinesis client
kinesis_client = boto3.client("kinesis", region_name="us-east-1")

# Set up Twitter API
twitter_auth = tweepy.OAuthHandler("API_KEY", "API_SECRET")
twitter_auth.set_access_token("ACCESS_TOKEN", "ACCESS_SECRET")
api = tweepy.API(twitter_auth)

def stream_tweets():
    for tweet in tweepy.Cursor(api.search_tweets, q="AWS", lang="en").items(100):
        tweet_data = {"tweet_id": tweet.id, "text": tweet.text, "user": tweet.user.screen_name}
        kinesis_client.put_record(StreamName="TwitterStream", Data=json.dumps(tweet_data), PartitionKey="default")

stream_tweets()
```

### **2️⃣ Data Processing (AWS Glue)**
📄 data_processing/glue_etl.py
```python
import sys
import boto3
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.dynamicframe import DynamicFrame

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

df = spark.read.json("s3://twitter-sentiment-data/*.json")

df_cleaned = df.selectExpr("tweet_id", "text", "timestamp", "user")

dynamic_frame = DynamicFrame.fromDF(df_cleaned, glueContext, "dynamic_frame")

glueContext.write_dynamic_frame.from_options(
    frame=dynamic_frame,
    connection_type="s3",
    connection_options={"path": "s3://twitter-sentiment-processed/"},
    format="json"
)
```

### **3️⃣ Sentiment Analysis with Amazon Comprehend**
📄 sentiment_analysis/lambda_sentiment.py
```python
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
```

### **4️⃣ REST API (AWS API Gateway + Lambda)**
📄 api_gateway/lambda_api.py
```python
import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("TwitterSentimentAnalysis")

def lambda_handler(event, context):
    tweet_id = event["queryStringParameters"]["tweet_id"]
    response = table.get_item(Key={"tweet_id": tweet_id})
    
    return {"statusCode": 200, "body": json.dumps(response["Item"])}
```

### **5️⃣ Visualization with QuickSight**
📄 visualization/quicksight_dashboard.md
```markdown
# 📊 QuickSight Dashboard Setup
1. **Enable AWS QuickSight** from AWS Console.
2. **Connect to Athena** using the `tweets_sentiment` table.
3. **Create a Dashboard** with:
   - 📈 **Line Chart** → Sentiment trend over time.
   - 📊 **Pie Chart** → Sentiment distribution.
   - ☁️ **Word Cloud** → Frequent words in sentiment categories.
```

---

## 📈 Sample API Request
```bash
curl "https://abc123.execute-api.us-east-1.amazonaws.com/prod/sentiment?tweet_id=12345"
```

📌 Response Example:
```json
{
  "tweet_id": "12345",
  "user": "elonmusk",
  "text": "Tesla stock is booming!",
  "sentiment": "Positive"
}
```

---

## 📌 Future Enhancements
1. 🔔 SNS Alerts for trending negative sentiments.
2. 🤖 Chatbot Integration to fetch sentiment insights via Slack.
3. 📡 Machine Learning to improve sentiment predictions.

---

## 💡 Credits
Developed by:
1. [Shubham Kulkarni](https://github.com/Shubham-andy7)
2. [Aman Gupta](https://github.com/amangupta05)
