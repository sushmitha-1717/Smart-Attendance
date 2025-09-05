🧩 Cloud-based Smart Attendance System

This project is a Smart Attendance Tracking System built using AWS Cloud Services and Flask (Python).
It captures attendance automatically using Amazon Rekognition (Face Recognition), stores results in DynamoDB, and displays attendance records with user images in a Flask web dashboard.

📌 Features

🖼️ Upload face images to S3 (reference bucket)

📷 Capture real-time images into S3 (test bucket)

🔎 Compare faces with Amazon Rekognition

🗄️ Store attendance logs in DynamoDB (user_id, timestamp, status)

🌐 View attendance in a Flask web app (with names, time, status, and images)

🏗️ Architecture

Components Used:

Amazon S3 → Stores test & reference images

Amazon Rekognition → Face matching

AWS Lambda → Triggered on image upload, runs comparison logic

Amazon DynamoDB → Stores attendance records

Amazon CloudWatch → Logs Lambda execution

Flask (Python) → Web dashboard frontend

⚙️ Setup Instructions
1. AWS Configuration

Create 2 S3 buckets:

main-images-bucketXXX → store reference images

test-images-bucketXXX → store real-time images

Create DynamoDB table: AttendanceTableXXX

Partition Key: user_id (String)

Create IAM Role/User with:

AmazonS3ReadOnlyAccess

AmazonRekognitionFullAccess

AmazonDynamoDBFullAccess

CloudWatchLogsFullAccess

2. Lambda Setup

Create Lambda function FaceAttendanceTrigger (Python 3.13)

Add S3 Trigger on test-images-bucketXXX (event: PUT)

Deploy Lambda code (face recognition + DynamoDB insert)

3. Flask App Setup

Install requirements:

pip install flask boto3


Configure AWS credentials locally:

aws configure


Enter Access Key, Secret Key, and Region (e.g., ap-south-1)

Run Flask app:

python app.py


Open browser:
http://127.0.0.1:5000/  

The Flask app shows a simple attendance table:

STATUS	USER_ID	TIMESTAMP	IMAGE
present	nandini	2025-09-05T07:33:22.692	🖼️ User Img
present	kavya	2025-09-05T07:26:29.043	🖼️ User Img
present	sushmitha	2025-09-05T07:40:10.128	🖼️ User Img
present	anjali	2025-09-05T07:42:33.781	🖼️ User Img
present	gowthami	2025-09-05T07:45:01.552	🖼️ User Img
present	srilatha	2025-09-05T07:48:19.334	🖼️ User Img
📂 Project Structure
attendance-system/
│── app.py               # Flask backend
│── templates/
│    └── table.html      # Frontend (dashboard)
│── requirements.txt     # Dependencies
│── README.md            # Documentation
