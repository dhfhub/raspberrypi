#!/bin/bash

ffmpeg -r 15 -use_wallclock_as_timestamps 1 -copytb 0 -f v4l2 -vcodec h264 -i /dev/video0 -vcodec copy -f flv rtmp://127.0.0.1:1935/hls/movie
#ffmpeg -r 15 -use_wallclock_as_timestamps 1 -copytb 0 -f v4l2 -vcodec h264 -i /dev/video0 -vcodec copy -f flv rtmp://127.0.0.1:1935/live
