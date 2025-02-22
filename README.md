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

## 📂 Project Structure
```
📦 twitter-sentiment-analysis-aws
│── 📂 data_ingestion
│   ├── kinesis_stream_setup.py
│   ├── lambda_producer.py
│── 📂 data_processing
│   ├── glue_etl.py
│── 📂 sentiment_analysis
│   ├── lambda_sentiment.py
│── 📂 api_gateway
│   ├── lambda_api.py
│── 📂 visualization
│   ├── quicksight_dashboard.md
│── 📂 infrastructure
│   ├── terraform.tf  # Terraform script to deploy AWS resources (Optional)
│── 📂 scripts
│   ├── fetch_tweets.py
│   ├── test_api.py
│── 📜 README.md
│── 📜 requirements.txt
│── 📜 .gitignore
```

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
