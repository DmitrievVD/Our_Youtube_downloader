from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Value_video(object):
    def setupUi(self, Value_video):
        Value_video.setObjectName("Value_video")
        Value_video.resize(271, 189)
        self.label_vibor = QtWidgets.QLabel(Value_video)
        self.label_vibor.setGeometry(QtCore.QRect(10, 20, 241, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_vibor.setFont(font)
        self.label_vibor.setObjectName("label_vibor")
        self.comboBox_value = QtWidgets.QComboBox(Value_video)
        self.comboBox_value.setGeometry(QtCore.QRect(20, 70, 73, 22))
        self.comboBox_value.setEditable(False)
        self.comboBox_value.setCurrentText("")
        self.comboBox_value.setObjectName("comboBox_value")
        self.download_video_btn = QtWidgets.QPushButton(Value_video)
        self.download_video_btn.setGeometry(QtCore.QRect(20, 110, 141, 41))
        self.download_video_btn.setObjectName("download_video_btn")

        self.retranslateUi(Value_video)
        QtCore.QMetaObject.connectSlotsByName(Value_video)

    def retranslateUi(self, Value_video):
        _translate = QtCore.QCoreApplication.translate
        Value_video.setWindowTitle(_translate("Value_video", "Качество"))
        self.label_vibor.setText(_translate("Value_video", "Выберите качество видео"))
        self.download_video_btn.setText(_translate("Value_video", "Скачать"))
