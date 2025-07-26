import boto3
import urllib.parse

s3 = boto3.client('s3')
sns = boto3.client('sns')

SNS_TOPIC_ARN = 'arn:aws:sns:ap-south-1:845488705635:resume-upload-alerts'

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(record['s3']['object']['key'])
        
        message = f"New resume uploaded:\nBucket: {bucket}\nFile: {key}"
        
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="New Resume Uploaded",
            Message=message
        )
    return {'statusCode': 200, 'body': 'Notification sent'}
