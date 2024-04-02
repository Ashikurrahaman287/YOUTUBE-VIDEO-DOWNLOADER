YouTube Video Downloader

This Python script allows you to download YouTube videos easily using the pytube library.

Requirements:
- Python 3.x
- pytube library (install via pip: `pip install pytube`)

Usage:
1. Run the script by executing `python youtube_downloader.py`.
2. Enter the YouTube video URL when prompted.
3. The script will download the highest resolution MP4 video available for the provided URL.

Example:
```
$ python youtube_downloader.py
Enter the YouTube video URL: [insert YouTube video URL here]
Downloading: [video title]
Download completed!
```

Note:
- Make sure you have a stable internet connection while downloading videos.
- The downloaded video will be saved in the same directory as the script by default. You can specify a different directory by modifying the `path` parameter in the `download_video()` function.

Author:
Ashikur Rahaman
Ashik@Spudblocks.com
