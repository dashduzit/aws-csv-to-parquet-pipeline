# AWS CSV → Parquet Pipeline

This project automates converting CSV files in S3 to Parquet format using an AWS Lambda function.

## 🧩 Overview
- Trigger: S3 `ObjectCreated:*` events for `.csv` files
- Language: **Python 3.12**
- Libraries: `boto3`, `pandas`, `pyarrow`
- Output: Parquet files written back to the same S3 bucket

## ⚙️ How It Works
1. A `.csv` file is uploaded to your S3 bucket.
2. The Lambda function reads it into a pandas DataFrame.
3. It converts the DataFrame to a Parquet table using `pyarrow`.
4. The resulting `.parquet` file is uploaded to S3 under the same key.

## 📦 Deployment
1. Create a Lambda function in AWS:
   - Runtime: **Python 3.12**
   - Handler: `lambda_function.lambda_handler`
2. Give it permissions:
   - `AWSLambdaBasicExecutionRole`
   - `s3:GetObject`, `s3:PutObject`, and `s3:ListBucket`
3. Add an S3 trigger for `.csv` uploads.
4. Use a **Lambda Layer** that includes:
   - `pandas`
   - `pyarrow`

## 🧠 What I Learned
This was my first end-to-end data pipeline project in the cloud. I built it while I was learning how serverless processing works in AWS and how data formats impact performance. 


