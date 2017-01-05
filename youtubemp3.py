import youtube_dl
import sys

url = sys.argv[-1]

options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320'
    }]
}

with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([url])
