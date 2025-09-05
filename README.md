Key Features

📷 Automatic Attendance → Upload real-time images, system matches with stored faces

🖼 Amazon Rekognition → Detects and verifies users with high accuracy

🗄 Amazon DynamoDB → Stores attendance logs (user_id, timestamp, status)

🪣 Amazon S3 → Stores both reference images and real-time captured images

🌐 Flask Dashboard → Displays attendance records with names, time, status & images

📊 CloudWatch Logs → Monitor Lambda executions

🏗️ System Architecture

Amazon S3 → Two buckets

main-images-bucket → Stores reference face images (e.g., nandini.jpg)

test-images-bucket → Stores uploaded real-time images

Amazon Rekognition → Compares uploaded images with reference images

AWS Lambda → Triggered on image upload, processes recognition and saves results

Amazon DynamoDB → Stores attendance records

Flask Web App → Displays attendance table with user images
<img width="1919" height="1123" alt="image" src="https://github.com/user-attachments/assets/8c42fa09-ef0c-434b-adeb-1a1c3a71c864" />
⚙️ Setup Instructions
1️⃣ AWS Setup

Create two S3 buckets:

main-images-bucket → store reference images

test-images-bucket → store real-time uploads

Create DynamoDB table: AttendanceTable

Partition key → user_id (String)

Create IAM Role/User with permissions:

AmazonS3ReadOnlyAccess

AmazonRekognitionFullAccess

AmazonDynamoDBFullAccess

CloudWatchLogsFullAccess

2️⃣ Lambda Setup

Function name: FaceAttendanceTrigger

Runtime: Python 3.13

Trigger: PUT event on test-images-bucket

Code: Rekognition + DynamoDB insert logic

3️⃣ Flask Setup (Local Dashboard)
# Clone repo
git clone https://github.com/your-username/attendance-system.git
cd attendance-system

# Install dependencies
pip install flask boto3

# Configure AWS credentials
aws configure
# (Enter Access Key, Secret Key, Region = ap-south-1)

# Run Flask app
python app.py


Visit 👉 http://127.0.0.1:5000/


📂 Project Structure
attendance-system/
│── app.py              
│── templates/
│    └── table.html      
│── requirements.txt     
│── README.md            

