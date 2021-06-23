# Get the image
# Uplaod the image

import boto3
import calendar
import time
import datetime
import os
from botocore.config import Config
from picamera import PiCamera

now = calendar.timegm(time.gmtime())

fresh_image_name = str(now) + ".jpg"
camera = PiCamera()
time.sleep(2)

print(datetime.datetime.now())
print("Taking a picture.")
camera.capture(fresh_image_name)
print("Picture Taken.")



upload_bucket = 'empakt.io'
upload_file_key = fresh_image_name

client = boto3.client('s3', 
                        aws_access_key_id = "AKIAILFOYVHW4RARGV6Q",
                        aws_secret_access_key = "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")

print("Uploading File.")
client.upload_file(fresh_image_name, upload_bucket, fresh_image_name)
print("File Uploaded.")

print("Delete File.")
os.remove(fresh_image_name)
print("File Deleted.")
