from pathlib import Path

from yt_dlp import YoutubeDL

url = input("Enter YouTube URL: ").strip()

download_dir = Path(__file__).resolve().parent / "downloads"
download_dir.mkdir(exist_ok=True)

options = {
    "format": "bestvideo+bestaudio/best",
    "merge_output_format": "mp4",
    "outtmpl": str(download_dir / "%(title)s.%(ext)s"),
    "noplaylist": True,
    "ffmpeg_location": r"C:\Users\girid\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg.Shared_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.1-full_build-shared\bin"
}

try:
    with YoutubeDL(options) as ydl:
        result = ydl.download([url])
    if result != 0:
        raise RuntimeError(f"yt-dlp returned exit code {result}")
    print(f"Download finished. Look in: {download_dir}")
except Exception as e:
    print(f"Download failed: {e}")