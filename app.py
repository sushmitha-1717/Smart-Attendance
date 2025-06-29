from flask import Flask, render_template
import boto3

app = Flask(__name__)


AWS_ACCESS_KEY = 'AKIAQE3ROL76MM3H4FRG'
AWS_SECRET_KEY = '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'
AWS_REGION = 'ap-south-1'
DYNAMO_TABLE = 'AttendanceTable22'
S3_BUCKET = 'test-images-bucket22'

dynamodb = boto3.resource(
    'dynamodb',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

s3 = boto3.client(
    's3',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

@app.route('/')
def index():
    table = dynamodb.Table(DYNAMO_TABLE)
    response = table.scan()
    items = response.get('Items', [])


    headers = set()
    for item in items:
        headers.update(item.keys())
    headers = list(headers)


    for item in items:
        image_found = False
        if 'user_id' in item:
            for ext in ['jpg', 'jpeg', 'png']:
                image_key = f'{item["user_id"]}.{ext}'
                public_url = f"https://{S3_BUCKET}.s3.amazonaws.com/{image_key}"
                try:
                    s3.head_object(Bucket=S3_BUCKET, Key=image_key)
                    item['image_url'] = public_url
                    image_found = True
                    break
                except:
                    continue
        if not image_found:
            item['image_url'] = '#'

    if 'image_url' not in headers:
        headers.append('image_url')

    return render_template('table.html', records=items, headers=headers)


if __name__ == '__main__':
    app.run(debug=True)
