# Resume Upload Notifier

A serverless application that allows users to upload resumes to an AWS S3 bucket, triggers a Lambda function, and sends an email notification to HR via SNS.

## Project Overview
- *Goal*: Enable users to upload resumes through a web form, store them in S3, and notify HR via email.
- *AWS Services Used*:
  - *S3*: Stores uploaded resumes.
  - *Lambda*: Processes uploads and sends notifications.
  - *SNS*: Sends email alerts to HR.
  - *IAM*: Secures access between services.
- *Features*:
  - HTML form for resume uploads.
  - Styled form with CSS for better user experience.
  - Event-driven architecture (S3 triggers Lambda, Lambda triggers SNS).

## Folder Structure
- lambda_function.py: Python code for the Lambda function that handles S3 events and sends SNS notifications.
- form.html: HTML form for uploading resumes to the S3 bucket.
- iam_policy.json: IAM permissions for Lambda to access S3 and SNS.
- css/style.css: CSS styles for the upload form.
- README.md: Project documentation (this file).

## How to Use
1. Open form.html in a web browser.
2. Select a .pdf or .docx file and click "Upload Resume".
3. Verify the file appears in the S3 bucket (uploads/ folder).
4. Check the HR email for an SNS notification with file details.

## Setup Instructions
1. Follow the project guide to configure S3, Lambda, SNS, and IAM.
2. Enable CORS on the S3 bucket for web uploads.
3. Host form.html locally or on a web server.
4. Test uploads to ensure Lambda and SNS work correctly.

## Skills Demonstrated
- Serverless architecture (Lambda, S3, SNS).
- Event-driven automation (S3 triggers Lambda).
- Web development (HTML, CSS).
- IAM roles and policies.
- Email notifications via SNS.
