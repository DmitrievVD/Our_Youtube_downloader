from pytube import YouTube
from PyQt5 import QtWidgets

def download_video(self, link, path):
    yt = YouTube(link)
    # print(yt.streams)
    yt.streams.get_highest_resolution().download(path, filename='first_video.mp4')
    QtWidgets.QMessageBox.information(self.frame, "Ура!!!", "Видео скачано!")

def download_audio(self,link, path):
    yt = YouTube(link)
    t=yt.streams.filter(only_audio=True).first()
    t.download(path, filename='first_audio.mp3')
    QtWidgets.QMessageBox.information(self.frame, "Ура!!!", "Аудио скачано!")