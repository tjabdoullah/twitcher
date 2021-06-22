# twitcher
a twitch extension to control your pi from a twitchbot

Source code to send Images to twitch
====================================
[TODO]

Type this in the browser
========================
https://id.twitch.tv/oauth2/authorize?client_id=ql4elwcibbxdc71nkl56cgziyskjpc&redirect_uri=http://localhost&response_type=token &scope=channel:moderate+chat:edit+chat:read

Get the token
=============
omxd7u8d3fqxzt7xu0vo3tsq1epc9z
ll2qg4231qavcerqjqtacq0nq6d2qa
















Timelapse
=========
Basically I need to capture then send pictures to S3 where I will view them later from a gallery or something, maybe even process a video based on the images and stream it, let's see

1- Upload images to AWS S3 with BOTO 3
install python3: [TODO]
install pip3: [sudo apt install python3-pip]
install boto3: [pip3 install boto3] #if you are running the cronjob as sudo, install it in sudo mode as well

2- Take pictures from the camera module
Install the camera library: [pip3 install picamera]

Cronjob
=======
Run the python code every 10 minutes
*/10 * * * * python3 /home/pi/Desktop/timelapse/theScreenShooter.py >> /home/pi/Desktop/timelapse/log.txt 2>&1


View the images
===============
It's better to download them with the AWS CLI [On mac there is a install file for that] using the following command:
aws s3 sync s3://empakt.io/ .

Transform the Images to a video
===============================
ffmpeg -framerate 1 -pattern_type glob -i '*.jpg' video.mp4

