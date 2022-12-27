from pytube import YouTube

# def getting_link(str_link: str):
#     ll = str_link
#     return ll

# def getting_path(str_path:str):
#     p = str_path
#     return p

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

# f_s = input("Введите ссылку: ")
# s_s = input("Введите путь:")

# first_str = "https://www.youtube.com/watch?v=D9G1VOjN_84"
# second_str = r"Homework_9\Project_2\Video"

# download_video(getting_link(f_s), getting_path(s_s))
# download_audio(getting_link(f_s), getting_path(s_s))


# download_video(getting_link(first_str), getting_path(second_str))
# download_audio(getting_link(first_str), getting_path(second_str))
