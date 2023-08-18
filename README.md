# Example AWS Lambda function + API Gateway + SES

## Setup 

1. Clone this repo
2. `cd aws-lambda-ses/`
3. In `notification/app.py` replace `YOUR_EMAIL_ADDRESS` with an email address you verify on SES ("Create identity" in Amazon SES console)
4. `sam build`
5. `sam deploy --guided`
6. Add the following policy to the Lambda function execution role (Configuration -> Permissions -> Execution role -> View the execution role in IAM console -> Create inline policy -> JSON tab)
```bash
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "ses:SendEmail",
      "ses:SendRawEmail"
    ],
    "Resource": "*"
  }]
}
```
7. Test in AWS Lambda Console with the `YOUR_EMAIL_ADDRESS` as the test event
```bash
{
  "body": "{\"email\": \"YOUR_EMAIL_ADDRESS\"}"
}
```

**Notes:**
Once you have verified your email address in SES, you can send emails to any email address. However, if you want to send emails to unverified email addresses, you need to request production access. See [here](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/request-production-access.html) for more details.