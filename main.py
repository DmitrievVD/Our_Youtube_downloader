from PyQt5 import QtWidgets
from inter import Ui_Form

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Form()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
    