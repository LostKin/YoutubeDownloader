from pytube import YouTube
import sys

video_format = {
    "resolution" : "720p",
    "fps" : "30fps",
    "mime_type" : "video/mp4",
}

vf = video_format

# RELEASE:
#s = input()
# DEBUG:
s = "https://www.youtube.com/watch?v=C9OMIberEnI"

yt = YouTube(s)
t = yt.streams.filter(res=vf["resolution"], mime_type=vf["mime_type"]).all()
yt.register_on_progress_callback(sup)
# DEBUG:
#for i in yt.streams.filter(res=vf["resolution"], mime_type=vf["mime_type"]).all():
#    print(i)
#t[0].on_download_progress(sup)

t[0].download()
