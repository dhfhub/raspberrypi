#!/bin/bash

HOST='127.0.0.1'
PORT='1935'
VideoSize='1280x720'

ffmpeg\
 -rtbufsize 100MB -f v4l2\
 -use_wallclock_as_timestamps 1\
 -copytb 0\
 -vcodec h264 -i /dev/video0\
 -vcodec copy\
 -f rtsp -rtsp_transport udp rtsp://$HOST:$PORT/hls/movie
