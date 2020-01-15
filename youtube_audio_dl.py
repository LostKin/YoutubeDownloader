from pytube import YouTube
s = input()
yt = YouTube(s)
#yt = yt.get('mp4', '720p')
t = yt.streams.filter(only_audio=True).all()
t[0].download()
