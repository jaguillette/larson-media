import boto3
import os
from datetime import datetime

s3 = boto3.resource('s3')
bucket = s3.Bucket('jagpublic')

for object in bucket.objects.filter(Prefix="photos"):
    filename, _, extension = object.key.replace("photos/", "").rpartition('.')
    today = datetime.now().strftime('%Y-%m-%d')

    # TODO: make and upload thumbnails if they don't exist in s3

    article_path = os.path.join(f"content", "photos", f"{filename}.md")
    if not os.path.exists(article_path):
        with open(article_path, "w") as fp:
            fp.write((f"Title: {filename}.{extension}\n"
                      f"Date: {today}\n"
                      f"thumbnail: thumbnails/{filename}.{extension}\n"
                      f"image: {filename}.{extension}\n"
                      f"tags: \n\n"
                      f"Generated in a batch"))
