# Smart-Attendance
This project involves creating a smart attendance tracking system that uses facial recognition to automatically mark student or employee attendance. It is integrated with AWS cloud services for storage, processing, and security, offering a scalable, contactless, and reliable attendance solution.

🧑‍💻 Smart Attendance Dashboard (AWS + Flask)
A cloud-based dashboard to visualize real-time attendance using AWS DynamoDB and display corresponding user photos from S3 — all in one elegant HTML table using Flask.

🚀 Features
Fetches real-time attendance data from DynamoDB

Auto-loads matching face images from AWS S3

Dynamically renders data in a clean HTML table

Displays photo (if found), user_id, timestamp, status, etc.

🧰 Tech Stack
Python (Flask, Boto3)

AWS DynamoDB (Attendance data)

AWS S3 (User images)

HTML / Jinja2 (Templating)

Bootstrap/CSS (for responsive table UI – optional)

📸 Sample UI
Automatically displays attendance data like:

Photo	User ID	Timestamp	Status
kavya	2025-07-01T09:20:33	Present

💻 Run Locally
📦 Clone the repo:

bash
Copy
Edit
git clone https://github.com/your-username/smart-attendance-dashboard.git
cd smart-attendance-dashboard
🔧 Install dependencies:

bash
Copy
Edit
pip install flask boto3
✍️ Update your AWS credentials and config:
In app.py:

python
Copy
Edit
AWS_ACCESS_KEY = 'YOUR_ACCESS_KEY'
AWS_SECRET_KEY = 'YOUR_SECRET_KEY'
AWS_REGION = 'ap-south-1'
DYNAMO_TABLE = 'AttendanceTable22'
S3_BUCKET = 'test-images-bucket22'
▶️ Run the app:

bash
Copy
Edit
python app.py
🌐 Open in browser:

cpp
Copy
Edit
http://127.0.0.1:5000
📦 Folder Structure
bash
Copy
Edit
├── app.py             # Flask app with DynamoDB + S3 integration
├── templates/
│   └── table.html     # Dynamic HTML table using Jinja2
✨ Optimizations
Automatically checks for jpg/jpeg/png images in S3

Skips image rendering if not found

Dynamically adapts to available data columns

🔐 AWS Permissions Needed
Attach these policies to your IAM user or role:

AmazonDynamoDBReadOnlyAccess

AmazonS3ReadOnlyAccess

✅ Ensure your S3 bucket has public access or a correct pre-signed URL policy.

🧪 Example S3 Bucket URL Format
php-template
Copy
Edit
https://<your-bucket>.s3.<region>.amazonaws.com/<user_id>.jpg
Example:

bash
Copy
Edit
https://test-images-bucket22.s3.ap-south-1.amazonaws.com/kavya.jpg
📬 Feedback / Issues
Feel free to open GitHub Issues or submit a PR if you'd like to contribute or suggest improvements!

🙏 Acknowledgements
Inspired by AWS Cloud Services and Smart Attendance ideas.
Data rendered using Flask and Boto3.

