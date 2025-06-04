from moviepy.editor import VideoFileClip

def cortar_e_converter_moviepy(input_file, output_file, start_minute=0, start_second=0, duration=59):
    start_time = start_minute * 60 + start_second

    clip = VideoFileClip(input_file).subclip(start_time, start_time + duration)

    # Se o vídeo for horizontal, cortar e redimensionar para 9:16
    w, h = clip.size
    if w > h:
        # calcular a largura ideal para manter altura e ter proporção 9:16
        new_width = int(h * 9 / 16)
        # cortar o centro horizontalmente
        x1 = (w - new_width) // 2
        x2 = x1 + new_width
        clip = clip.crop(x1=x1, y1=0, x2=x2, y2=h)

    # Salvar o resultado
    clip.write_videofile(output_file, codec='libx264', audio_codec='aac')

# Exemplo de uso:
input_video = "video_original.mp4"
output_video = "shorts_vertical.mp4"

cortar_e_converter_moviepy(input_video, output_video, start_minute=2, start_second=30, duration=59)
