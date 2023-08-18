import json
import boto3

client = boto3.client('ses', region_name='us-east-1')
source_email = 'YOUR_EMAIL_ADDRESS'

def lambda_handler(event, context):

    body = json.loads(event['body'])
    email = body['email']

    response = client.send_email(
    Destination={
        'ToAddresses': [email]
    },
    Message={
        'Body': {
            'Text': {
                'Charset': 'UTF-8',
                'Data': 'This is the message body in text format. Send via AWS SES.',
            }
        },
        'Subject': {
            'Charset': 'UTF-8',
            'Data': 'AWS SES Test email',
        },
    },
    Source=source_email
    )
    
    print(response)
    
    return {
        'statusCode': 200,
        'body': json.dumps("Email Sent Successfully. MessageId is: " + response['MessageId'])
    }