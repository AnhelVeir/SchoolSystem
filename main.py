from PyQt5 import QtWidgets, QtCore
import loginWindow
import mainApp
import sys


class TwoWindow(QtWidgets.QMainWindow, mainApp.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class OneWindow(QtWidgets.QMainWindow, loginWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.twoWindow = None
        self.enterbutton.clicked.connect(lambda: self.enter_app(self.loginEdit.text(), self.passwordEdit.text()))

    def enter_app(self, login, password):
        if login == "root" and password == "admin":
            print("ОГО")
            self.info_label.setText("Осуществляем вход")
            self.close()
            self.twoWindow = TwoWindow()
            self.twoWindow.show()
        else:
            self.info_label.setText("Неверный логин или пароль")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = OneWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
