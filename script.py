from pytube import Playlist, YouTube
from os import rename

link = input('Link: \n|> ')
mode = int(input('Mode: \n[0] MP4 VIDEO\n[1] MP4 AUDIO\n[2] MP3 AUDIO\n|> '))

def download(video):
    file = video.streams.get_audio_only().download() if mode > 0 else video.streams.get_highest_resolution().download()
    if mode == 2: rename(file, file[:-3]+'mp3')

if 'playlist' in link:
    for video in Playlist(link).videos:
        download(video)
        print(video.title)

else:
    video = YouTube(link)
    download(video)
    print(video.title)