from pytube import YouTube
from PyQt5 import QtWidgets
from pytube.cli import on_progress

def download_video(self, link, path):
    def on_progress_bar(stream, chunk: bytes, bytes_remaining: int) -> None:  # pylint: disable=W0613
        filesize = stream.filesize
        bytes_received = filesize - bytes_remaining
        finish = 100
        go = ((bytes_received * finish) / filesize)
        # print(go, finish)
        self.progressBar.setValue(int(go))
    yt = YouTube(link, on_progress_callback=on_progress_bar)
    strams = yt.streams.get_lowest_resolution()
    strams.download(path, filename='first_video.mp4')
    QtWidgets.QMessageBox.information(self.frame, "Ура!!!", "Видео скачано!")

def download_audio(self,link, path):
    def on_progress_bar(stream, chunk: bytes, bytes_remaining: int) -> None:  # pylint: disable=W0613
        filesize = stream.filesize
        bytes_received = filesize - bytes_remaining
        finish = 100
        go = ((bytes_received * finish) / filesize)
        # print(go, finish)
        self.progressBar.setValue(int(go))
    yt = YouTube(link, on_progress_callback=on_progress_bar)
    t=yt.streams.filter(only_audio=True).first()
    t.download(path, filename='first_audio.mp3')
    QtWidgets.QMessageBox.information(self.frame, "Ура!!!", "Аудио скачано!")