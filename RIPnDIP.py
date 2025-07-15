import yt_dlp

def Download(link, download_type):
    if download_type == 'video':
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
            'outtmpl': '%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
}

    elif download_type == 'wav':
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
            }],
        }
    else:
        print("Invalid choice.")
        return

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print(f"{download_type.capitalize()} Download Success")
    except Exception as e:
        print("Download Failed:", e)

link = input("Video URL: ")
choice = input("Download 'video' or 'wav': ").lower()
Download(link, choice)
input("Press Enter to exit...")
