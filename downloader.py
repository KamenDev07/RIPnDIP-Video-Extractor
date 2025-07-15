import yt_dlp

def download_media(url, format_choice):
    ydl_opts = {}

    if format_choice in ['mp3', 'wav']:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': format_choice,
                'preferredquality': '192',
            }],
        }
    elif format_choice == 'mp4':
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
        }
    else:
        print("Unsupported format selected.")
        return

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = input("Enter the video URL: ")
    format_choice = input("Enter desired format (mp3, wav, mp4): ").lower()
    download_media(url, format_choice)
