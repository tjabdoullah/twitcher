
# twitcher
a twitch extension to control your pi from a twitchbot while streaming


## 0/ Project Structure
The codebase is currently half python half nodejs. The node js part connects to a twitch bot to be able to receive messages from the chat. Once a message is recieved, based on if it's left or right, a python script recieves the direction for the stepper motor to rurn either right or left.

    node express_app/index.js

## 1/ To stream you need a client ID & a Key that you need to get from
https://id.twitch.tv/oauth2/authorize?client_id=[your client ID]&redirect_uri=http://localhost&response_type=token &scope=channel:moderate+chat:edit+chat:read

## 2/ Send the camera module stream to twitch

**Set width and height of output video**

    WIDTH=1920
    HEIGHT=1080

**Set output framerate**

    FRAMERATE=30

**Set keyframe spacing (must be double the framerate)**

    KEYFRAME=60

**Set bitrate (Twitch recommends 3500000)**

    BITRATE=3500000

**Set stream URL**

    URL=rtmp://maa01.contribute.live-video.net/app

**Set stream key**

    KEY=live_101362215_q17lXWrNVX8nB8E8OmCiFw05XedLdG

**Command**

    raspivid -n -t 0 -w $WIDTH -h $HEIGHT -fps $FRAMERATE -b $BITRATE -g $KEYFRAME -o - | ffmpeg -f lavfi -i anullsrc -c:a aac -r $FRAMERATE -i - -g $KEYFRAME -strict experimental -threads 4 -vcodec copy -map 0:a -map 1:v -b:v $BITRATE -preset ultrafast -f flv "${URL}/${KEY}"

## 4/ As long as you are streaming, maybe you want to have a time lapse ##
Basically I need to capture then send pictures to S3 where I will view them later from a gallery or something, maybe even process a video based on the images and stream it, let's see

1- Upload images to AWS S3 with BOTO 3
install python3
install pip3:

    sudo apt install python3-pip

install boto3

    pip3 install boto3

2- Take pictures from the camera module

    pip3 install picamera

## 5/ Cronjob ##
Run the python code every 10 minutes

    */10 * * * * python3 /home/pi/Desktop/timelapse/theScreenShooter.py >> /home/pi/Desktop/timelapse/log.txt 2>&1

## 6/ View the images ##
It's better to download them with the AWS CLI [On mac there is a install file for that] using the following command:

    aws s3 sync s3://empakt.io/ .

## 7/ Transform the Images to a video

    ffmpeg -framerate 1 -pattern_type glob -i '*.jpg' video.mp4

