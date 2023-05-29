from pytube import YouTube

def download_video(url, resolution=None, output_path=None):
    yt = YouTube(url)
    
    # best resolution
    if resolution is None:
        stream = yt.streams.get_highest_resolution()
    else:
        stream = yt.streams.get_by_resolution(resolution)
    
    if output_path is None:
        output_path = "./"
    
    # download
    print(f"Downloading: {stream.title}")
    stream.download(output_path=output_path)
    print("Download complete!")

if __name__ == '__main__':
    # example
    video_url = input("Enter YouTube video URL: ")
    video_resolution = input("Enter desired video resolution (optional): ")
    download_video(video_url, resolution=video_resolution)
