import os
import io
import boto3
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

s3 = boto3.client('s3')
def lambda_handler(event, context):
    # Read ad the CSV file from S3
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    obj = s3.get_object(Bucket=bucket, Key=key)
    df = pd.read_csv(io.BytesIO(obj['Body'].read()))
    # Convert the DataFrame to a PyArrow Table
    table = pa.Table.from_pandas(df)
    # Write the PyArrow Table to a Parquet file in memory
    parquet_buffer = io.BytesIO()
    pq.write_table(table, parquet_buffer)
    # Upload the Parquet file to S3 (same location,but .parquet instead of .csv)
    s3.put_object(Bucket=bucket, Key=key.replace('.csv', '.parquet'), Body=parquet_buffer.getvalue())

    return {
        "statusCode": 200,
        "body": "File converted to Parquet and uploaded to S3"
    }


