from funcs import download_audio, download_video
from PyQt5 import QtWidgets

def start_button_click(self):
    if len(self.video_link.toPlainText()) > 10:
        if len(self.path_file.toPlainText()) > 0:
            link = self.video_link.toPlainText()
            path = self.path_file.toPlainText()
            if self.radioButton_video.isChecked():
                download_video(link, path)
            else:
                download_audio(link, path)
        else:
            QtWidgets.QMessageBox.warning(self.frame,"Ошибка!","Вы не выбрали папку для сохранения!")
    else:
        QtWidgets.QMessageBox.warning(self.frame ,"Ошибка!","Укажите ссылку на видео!")

def button_directorie_click(self):
    directorie_path = QtWidgets.QFileDialog.getExistingDirectory(parent= self.frame, caption='Choose directorie: ',directory=r'C:\Users\User\Desktop' )
    self.path_file.setPlainText(directorie_path)