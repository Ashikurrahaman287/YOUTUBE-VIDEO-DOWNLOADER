from pytube import YouTube

def download_video(url, path='./'):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if video:
            print(f'Downloading: {yt.title}')
            video.download(output_path=path)
            print('Download completed!')
        else:
            print('No progressive MP4 stream available for this video.')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)
