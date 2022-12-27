from pytube import YouTube

def download_video(link, path):
    yt = YouTube(link)
    # print(yt.streams)
    yt.streams.get_highest_resolution().download(path, filename='first_video.mp4')
    print("Видео успешно загружено")

def download_audio(link, path):
    yt = YouTube(link)
    t=yt.streams.filter(only_audio=True).first()
    t.download(path, filename='first_audio.mp3')
    print("Аудио успешно загружено")
