import os
import yt_dlp

# Dossier de téléchargement
DOWNLOAD_FOLDER = "C:/Users/NGUESSAN.DESKTOP-38E6PIP/Desktop/Musikys/"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def download_youtube(youtube_url, mode="3"):
    try:
        if mode == "3":
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
        elif mode == "4":
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
                'merge_output_format': 'mp4',
            }
        else:
            print("⚠️ Mode invalide. Tape 3 pour MP3 ou 4 pour MP4.")
            return

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])

        print("✅ Téléchargement terminé avec succès !")

    except Exception as e:
        print(f"❌ Erreur : {e}")

if __name__ == "__main__":
    print("🎵 YouTube Downloader (MP3/MP4) 🎵")
    while True:
        url = input("\n🔗 Entrez un lien YouTube (ou CTRL + C pour quitter) : ").strip()
        if url:
            mode = input("🎚 Tape 3 pour MP3 ou 4 pour MP4 : ").strip()
            download_youtube(url, mode)
