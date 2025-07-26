# Resume Upload Notifier

A project to upload resumes to an S3 bucket, trigger a Lambda function, and send an email to HR via SNS.

## Files
- lambda_function.py: Code for the Lambda function.
- form.html: Webpage for uploading resumes.
- iam_policy.json: Permissions for Lambda.
- README.md: This file.

## How to Use
1. Open form.html in a browser.
2. Upload a .pdf or .docx file.
3. Check the S3 bucket and HR email for the file and notification.