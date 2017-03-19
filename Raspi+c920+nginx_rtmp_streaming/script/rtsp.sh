#!/bin/bash

HOST='192.168.0.6'
PORT='1234'
VideoSize='1280x720'

ffmpeg\
 -rtbufsize 100MB -f v4l2\
 -use_wallclock_as_timestamps 1\
 -copytb 0\
 -video_size $VideoSize -vcodec h264 -i /dev/video0\
 -loglevel info -copyinkf\
 -vcodec copy\
 -f rtsp -rtsp_transport tcp rtsp://$HOST:$PORT/live.sdp
