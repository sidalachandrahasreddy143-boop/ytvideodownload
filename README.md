🎬 YouTube Video Downloader
A simple Python-based YouTube video downloader that allows users to download videos and playlists in MP4 format with high-quality audio and video.
✨ Features

Download YouTube videos using their URLs.
Download videos with high-quality audio and video.
Automatically merge video and audio into MP4 format.
Support playlist downloads.
Automatically create a downloads folder.
Simple command-line interface.
Uses FFmpeg for audio and video merging.

🛠️ Technologies Used

Python: Main programming language.
yt-dlp: Video downloading library.
FFmpeg: Audio and video processing.

📂 Project Structure
videoDownloding/
│
├── downloads/
├── video.py
├── requirements.txt
├── README.md
└── .gitignore

⚙️ Installation
1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL

2. Navigate to the project folder
cd videoDownloding

3. Create a virtual environment
python -m venv .venv

4. Activate the virtual environment
Windows:
.venv\Scripts\activate

5. Install dependencies
pip install -r requirements.txt

6. Install FFmpeg
Install FFmpeg and make sure it is accessible from your system PATH.
▶️ How to Run
Run the Python application:
python video.py

Enter the YouTube video URL when prompted.
The downloaded video will be saved in the downloads folder.
🔮 Future Improvements

Build a graphical user interface (GUI).
Add video quality selection.
Support multiple video formats.
Display download progress.
Add download history.
Improve error handling.

⚠️ Disclaimer
This project is intended for educational purposes. Download only content that you own or have permission to download, and follow YouTube's terms and applicable copyright laws.
👨‍💻 Author
Chandrahas Reddy
GitHub: https://github.com/sidalachandrahasreddy143-boop

⭐ If you find this project useful, consider giving it a star!
