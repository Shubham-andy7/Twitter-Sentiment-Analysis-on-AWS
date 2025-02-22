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
