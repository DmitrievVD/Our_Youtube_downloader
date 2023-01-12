from pytube import YouTube
from PyQt5 import QtWidgets
import time
from value_video import Ui_Value_video


def value_video(self, link, path):
    global Value_video
    Value_video = QtWidgets.QWidget()
    ui = Ui_Value_video()
    ui.setupUi(Value_video)
    Value_video.show()

    def value(link):
        yt = YouTube(link)
        values = set()
        for stream in yt.streams.filter(type="video"):
            values.add(stream.resolution)
        streams = sorted(values)
        ui.comboBox_value.addItems(streams)

    def download_video_btn():
        value = ui.comboBox_value.currentText()
        def download_video(self, link, path, val):
            Value_video.close()
            def on_progress_bar(stream, chunk: bytes, bytes_remaining: int) -> None:  # pylint: disable=W0613
                filesize = stream.filesize
                bytes_received = filesize - bytes_remaining
                finish = 100
                go = ((bytes_received * finish) / filesize)
                self.progressBar.setValue(int(go))
                time.sleep(0.009)

            yt = YouTube(link, on_progress_callback=on_progress_bar)
            strams = yt.streams.filter(resolution=val).first()
            if len(self.file_name.toPlainText()) > 1:
                strams.download(path, filename=self.file_name.toPlainText() + '.mp4')
            else:
                strams.download(path, filename='new_video.mp4')
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText('Download compleat!!!')
            msg.setWindowTitle('Already!')
            msg.addButton("Ok", QtWidgets.QMessageBox.RejectRole)
            retval = msg.exec_()
        download_video(self, link, path, value)

    value(link)
    ui.download_video_btn.clicked.connect(download_video_btn)

def download_audio(self,link, path):
    def on_progress_bar(stream, chunk: bytes, bytes_remaining: int) -> None:  # pylint: disable=W0613
        filesize = stream.filesize
        bytes_received = filesize - bytes_remaining
        finish = 100
        go = ((bytes_received * finish) / filesize)
        self.progressBar.setValue(int(go))
        time.sleep(0.0009)
    yt = YouTube(link, on_progress_callback=on_progress_bar)
    t=yt.streams.filter(only_audio=True).first()
    if len(self.file_name.toPlainText()) > 1:
        t.download(path, filename=(self.file_name.toPlainText() + '.mp3'))
    else:
        t.download(path, filename='new_audio.mp3')
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setText('Download compleat!!!')
    msg.setWindowTitle('Already!')
    msg.addButton("Ok", QtWidgets.QMessageBox.RejectRole)
    retval = msg.exec_()
    