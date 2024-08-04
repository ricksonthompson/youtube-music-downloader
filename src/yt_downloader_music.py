import json
import yt_dlp

def download_audio_from_youtube(url, name):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{name}.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print(f"Download e conversão concluídos: {name}.mp3")
    except Exception as e:
        print(f"Erro ao baixar ou converter o vídeo: {e}")

with open('input/urls.json', 'r') as file:
    data = json.load(file)

for item in data:
    url = item['url']
    name = item['name']
    download_audio_from_youtube(url, name)