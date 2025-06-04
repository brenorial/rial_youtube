# 🎥 YouTube Video Downloader com yt_dlp

Este projeto é um script simples em Python que baixa vídeos do YouTube utilizando a biblioteca [`yt_dlp`](https://github.com/yt-dlp/yt-dlp), uma versão aprimorada do `youtube-dl`.

---

## ✅ Requisitos

- Python 3.7 ou superior
- `yt_dlp` instalado

### 📦 Instalação

1. Clone o repositório ou copie o script:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
````

2. Instale a biblioteca `yt_dlp`:

```bash
pip install yt-dlp
```

---

## 🚀 Como usar

Edite o script `baixar.py` com a URL desejada:

```python
youtube_url = ""
output_name = "video_original.mp4"
```

Depois, execute:

```bash
python baixar.py
```

O vídeo será salvo como `video_original.mp4` na mesma pasta.

---

## ⚙️ Personalização

Você pode alterar o nome do arquivo de saída modificando a variável `output_name`, ou ajustar a qualidade do vídeo modificando a opção `format` no dicionário `ydl_opts`.

---
