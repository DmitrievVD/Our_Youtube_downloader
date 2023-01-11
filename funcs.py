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

    def download_video_btn():
        value = ui.comboBox_value.currentText()
        print(value)
        def download_video(self, link, path):
            Value_video.close()
            def on_progress_bar(stream, chunk: bytes, bytes_remaining: int) -> None:  # pylint: disable=W0613
                filesize = stream.filesize
                bytes_received = filesize - bytes_remaining
                finish = 100
                go = ((bytes_received * finish) / filesize)
                # print(go, finish)
                self.progressBar.setValue(int(go))
                time.sleep(0.009)

            yt = YouTube(link, on_progress_callback=on_progress_bar)
            strams = yt.streams.get_lowest_resolution()
            if len(self.file_name.toPlainText()) > 1:
                strams.download(path, filename=self.file_name.toPlainText() + '.mp4')
            else:
                strams.download(path, filename='new_video.mp4')
            QtWidgets.QMessageBox.information(self.frame, "Ура!!!", "Видео скачано!")

        download_video(self, link, path)

    def value(link):
        yt = YouTube(link)
        streams = set()

        for stream in yt.streams.filter(type="video"):
            streams.add(stream.resolution)

        ui.comboBox_value.addItems(streams)

    value(link)



    ui.download_video_btn.clicked.connect(download_video_btn)







<<<<<<< HEAD
def download_video(self, link, path):
    def on_progress_bar(stream, chunk: bytes, bytes_remaining: int) -> None:  # pylint: disable=W0613
        filesize = stream.filesize
        bytes_received = filesize - bytes_remaining
        finish = 100
        go = ((bytes_received * finish) / filesize)
        self.progressBar.setValue(int(go))
        time.sleep(0.01)
    
    yt = YouTube(link, on_progress_callback=on_progress_bar)
    strams = yt.streams.get_lowest_resolution()
    if len(self.file_name.toPlainText()) > 1:
        strams.download(path, filename=self.file_name.toPlainText()+ '.mp4')
    else:
        strams.download(path, filename='new_video.mp4')
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setText("Download Compleat!")
    msg.setWindowTitle("Already!")
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.setEscapeButton(QtWidgets.QMessageBox.StandardButton)
    retval = msg.exec_()
  
    # QtWidgets.QMessageBox().question(self.frame, "Ура!!!", "Видео скачано! Продолжить?", QtWidgets.QMessageBox.StandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No))
    # QtWidgets.QMessageBox.setStandardButtons(QtWidgets.QMessageBox,| QtWidgets.QMessageBox.Ok)
=======
    

>>>>>>> 77090e867bf11857888243e4202fbd1f36867c90

def download_audio(self,link, path):
    def on_progress_bar(stream, chunk: bytes, bytes_remaining: int) -> None:  # pylint: disable=W0613
        filesize = stream.filesize
        bytes_received = filesize - bytes_remaining
        finish = 100
        go = ((bytes_received * finish) / filesize)
        self.progressBar.setValue(int(go))
        time.sleep(0.01)
    yt = YouTube(link, on_progress_callback=on_progress_bar)
    t=yt.streams.filter(only_audio=True).first()
    if len(self.file_name.toPlainText()) > 1:
        t.download(path, filename=(self.file_name.toPlainText() + '.mp3'))
    else:
        t.download(path, filename='new_audio.mp3')
    QtWidgets.QMessageBox.information(self.frame, "Ура!!!", "Аудио скачано!")