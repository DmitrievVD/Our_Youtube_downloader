from pytube import YouTube
from PyQt5 import QtWidgets
import time

def download_video(self, link, path):
    def on_progress_bar(stream, chunk: bytes, bytes_remaining: int) -> None:  # pylint: disable=W0613
        filesize = stream.filesize
        bytes_received = filesize - bytes_remaining
        finish = 100
        go = ((bytes_received * finish) / filesize)
        # print(go, finish)
        self.progressBar.setValue(int(go))
        time.sleep(0.0009)
    
    yt = YouTube(link, on_progress_callback=on_progress_bar)
    strams = yt.streams.get_lowest_resolution()
    if len(self.file_name.toPlainText()) > 1:
        strams.download(path, filename=self.file_name.toPlainText()+ '.mp4')
    else:
        strams.download(path, filename='new_video.mp4')
    QtWidgets.QMessageBox.information(self.frame, "Ура!!!", "Видео скачано!")

def download_audio(self,link, path):
    def on_progress_bar(stream, chunk: bytes, bytes_remaining: int) -> None:  # pylint: disable=W0613
        filesize = stream.filesize
        bytes_received = filesize - bytes_remaining
        finish = 100
        go = ((bytes_received * finish) / filesize)
        # print(go, finish)
        self.progressBar.setValue(int(go))
        time.sleep(0.0009)
    yt = YouTube(link, on_progress_callback=on_progress_bar)
    t=yt.streams.filter(only_audio=True).first()
    if len(self.file_name.toPlainText()) > 1:
        t.download(path, filename=(self.file_name.toPlainText() + '.mp3'))
    else:
        t.download(path, filename='new_audio.mp3')
    QtWidgets.QMessageBox.information(self.frame, "Ура!!!", "Аудио скачано!")