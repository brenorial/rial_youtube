import yt_dlp


youtube_url = ""  
output_name = "video_original.mp4"

def baixar_video(url):
    ydl_opts = {
        'format': 'mp4', 
        'outtmpl': output_name,
        'merge_output_format': 'mp4',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

baixar_video(youtube_url)
print(f"✅ Vídeo baixado com sucesso: {output_name}")
