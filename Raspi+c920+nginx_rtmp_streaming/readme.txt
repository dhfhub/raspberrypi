• ffmpeg
• gcc
• make
• lib32-openssl
• git
• v4l-utils
sudo apt-get install ffmpeg gcc make libssl-dev v4l-utils

•Compile nginx with rtmp module
git clone https://github.com/arut/nginx-rtmp-module.git

http://nginx.org/download/
wget http://nginx.org/download/nginx-1.9.9.tar.gz
tar -zxvf ...tar.gz

cd nginx-1.**/
./configure --add-module=../nginx-rtmp-module
make
sudo make install
make clean

./configure: error: the HTTP rewrite module requires the PCRE library.
sudo apt-get install libpcre3 libpcre3-dev


•Setup nginx
create directory /tmp/hls and chmod 777
edit /usr/local/nginx/conf/nginx.conf



以下のようにinitスクリプトを使い自動起動
sudo wget https://raw.githubusercontent.com/JasonGiedymin/nginx-init-ubuntu/master/nginx -O /etc/init.d/nginx
sudo chmod +x /etc/init.d/nginx
sudo update-rc.d nginx defaults
スクリプトを用意すればいつものように起動＆停止が可能です。
sudo service nginx start
sudo service nginx stop



•setup JWPlayer KEY:M3MuDEg+S+keZ3ryBjxR2cRrRxMh7P/F6jKYaw==
JWPlayerに登録しダウンロード
Extract the contents to /usr/local/nginx/html/jwplayer
unzip jwplayer-7.9.3.zip
sudo mv jwplayer-7.9.3 /usr/local/nginx/html/jwplayer

Modify /usr/local/nginx/html/index.html
Remember to adjust the playlist.sources.file path to your ip address.

Start nginx:
sudo /usr/local/nginx/sbin/nginx


•setup ffmpeg
Change resolution of your output

v4l2-ctl --device=/dev/video0 --set-fmt-video=width=1280,height=720,pixelformat=1


•Stream to nginx
ffmpeg -r 15 -use_wallclock_as_timestamps 1 -copytb 0 -f v4l2 -vcodec h264 -i /dev/video0 -vcodec copy -f flv rtmp://127.0.0.1:1935/hls/movie

I use -r 15 and -use_wallclock_as_timestamps which solves the Incorrect dts errors of ffmpeg. This reduces performance a bit and you may want to use the timestamps without modification.


•使用手順
./rtmp.shを起動すれば動画が見れる
ではどんなイベントでrtmp.shを起動するようにしようか・・・

•
•
•
