# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class white_button(QtWidgets.QPushButton):
    def __init__(self, *args):
        super().__init__(*args)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.setFont(font)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(978, 668)
        MainWindow.setMinimumSize(978, 668)
        MainWindow.setStyleSheet("background-color: rgb(255, 250, 250);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1101, 801))
        self.tabWidget.setAccessibleName("")

        self.profile = QtWidgets.QWidget()
        self.profile.setEnabled(True)
        self.profile.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.profile.setMouseTracking(False)
        self.profile.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.profile.setAccessibleName("")

        self.profile.setObjectName("profile")
        self.label_info_about_teacher_lock = QtWidgets.QLabel(self.profile)
        self.label_info_about_teacher_lock.setGeometry(QtCore.QRect(30, 20, 411, 16))
        font_verdana_12 = QtGui.QFont()
        font_verdana_12.setFamily("Verdana")
        font_verdana_12.setPointSize(12)
        font_verdana_12.setBold(True)
        font_verdana_12.setWeight(75)
        self.label_info_about_teacher_lock.setFont(font_verdana_12)
        self.label_info_about_teacher_lock.setObjectName("label_info_about_teacher_lock")
        self.surname_label_lock = QtWidgets.QLabel(self.profile)
        self.surname_label_lock.setGeometry(QtCore.QRect(40, 70, 131, 16))
        font_verdana_12.setBold(False)
        self.surname_label_lock.setFont(font_verdana_12)

        self.name_label_lock = QtWidgets.QLabel(self.profile)
        self.name_label_lock.setGeometry(QtCore.QRect(40, 100, 131, 16))
        self.name_label_lock.setFont(font_verdana_12)

        self.patronymic_label_lock = QtWidgets.QLabel(self.profile)
        self.patronymic_label_lock.setGeometry(QtCore.QRect(40, 130, 131, 16))
        self.patronymic_label_lock.setFont(font_verdana_12)

        self.email_label_lock = QtWidgets.QLabel(self.profile)
        self.email_label_lock.setGeometry(QtCore.QRect(40, 160, 131, 16))
        self.email_label_lock.setFont(font_verdana_12)

        self.phone_label_lock = QtWidgets.QLabel(self.profile)
        self.phone_label_lock.setGeometry(QtCore.QRect(40, 190, 131, 16))
        self.phone_label_lock.setFont(font_verdana_12)

        self.class_label_lock = QtWidgets.QLabel(self.profile)
        self.class_label_lock.setGeometry(QtCore.QRect(40, 220, 131, 16))
        self.class_label_lock.setFont(font_verdana_12)

        self.surname_label = QtWidgets.QLabel(self.profile)
        self.surname_label.setGeometry(QtCore.QRect(190, 70, 131, 16))
        self.surname_label.setFont(font_verdana_12)

        self.name_label = QtWidgets.QLabel(self.profile)
        self.name_label.setGeometry(QtCore.QRect(190, 100, 131, 16))
        self.name_label.setFont(font_verdana_12)

        self.patronymic_label = QtWidgets.QLabel(self.profile)
        self.patronymic_label.setGeometry(QtCore.QRect(190, 130, 131, 16))
        self.patronymic_label.setFont(font_verdana_12)

        self.email_label = QtWidgets.QLabel(self.profile)
        self.email_label.setGeometry(QtCore.QRect(190, 160, 131, 16))
        self.email_label.setFont(font_verdana_12)

        self.phone_label = QtWidgets.QLabel(self.profile)
        self.phone_label.setGeometry(QtCore.QRect(190, 190, 131, 16))
        self.phone_label.setFont(font_verdana_12)

        self.class_label = QtWidgets.QLabel(self.profile)
        self.class_label.setGeometry(QtCore.QRect(190, 220, 131, 16))
        self.class_label.setFont(font_verdana_12)

        self.edit_email_lock = QtWidgets.QLabel(self.profile)
        self.edit_email_lock.setGeometry(QtCore.QRect(40, 290, 131, 16))
        self.edit_email_lock.setFont(font_verdana_12)

        self.new_email_lock = QtWidgets.QLabel(self.profile)
        self.new_email_lock.setGeometry(QtCore.QRect(40, 320, 131, 16))
        self.new_email_lock.setFont(font_verdana_12)

        self.email_edit = QtWidgets.QLineEdit(self.profile)
        self.email_edit.setGeometry(QtCore.QRect(180, 319, 171, 21))
        self.email_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        font_standart_12 = QtGui.QFont()
        self.email_edit.setFont(font_standart_12)

        self.password_confirm_1 = QtWidgets.QLineEdit(self.profile)
        self.password_confirm_1.setGeometry(QtCore.QRect(572, 320, 171, 21))
        self.password_confirm_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.password_confirm_1.setFont(font_standart_12)

        self.conf_pas_lock = QtWidgets.QLabel(self.profile)
        self.conf_pas_lock.setGeometry(QtCore.QRect(380, 320, 191, 16))
        self.conf_pas_lock.setFont(font_verdana_12)

        self.edit_email_button = white_button(self.profile)
        self.edit_email_button.setGeometry(QtCore.QRect(770, 312, 131, 31))

        self.new_phone_lock = QtWidgets.QLabel(self.profile)
        self.new_phone_lock.setGeometry(QtCore.QRect(40, 400, 131, 16))
        self.new_phone_lock.setFont(font_verdana_12)

        self.edit_phone_button = white_button(self.profile)
        self.edit_phone_button.setGeometry(QtCore.QRect(770, 392, 131, 31))

        self.phone_edit = QtWidgets.QLineEdit(self.profile)
        self.phone_edit.setGeometry(QtCore.QRect(180, 399, 171, 21))
        self.phone_edit.setFont(font_standart_12)
        self.phone_edit.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.password_confirm_2 = QtWidgets.QLineEdit(self.profile)
        self.password_confirm_2.setGeometry(QtCore.QRect(572, 400, 171, 21))
        self.password_confirm_2.setFont(font_standart_12)
        self.password_confirm_2.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.conf_pass2_lock = QtWidgets.QLabel(self.profile)
        self.conf_pass2_lock.setGeometry(QtCore.QRect(380, 400, 191, 16))
        self.conf_pass2_lock.setFont(font_verdana_12)

        self.edit_phone_lock = QtWidgets.QLabel(self.profile)
        self.edit_phone_lock.setGeometry(QtCore.QRect(40, 370, 231, 16))
        self.edit_phone_lock.setFont(font_verdana_12)

        self.tabWidget.addTab(self.profile, "")

        # Начало таблицы
        self.class_decr = QtWidgets.QWidget()

        self.tableWidget = QtWidgets.QTableWidget(self.class_decr)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setGeometry(QtCore.QRect(40, 110, 921, 411))
        colCount = 10
        self.tableWidget.setColumnCount(colCount)
        self.tableWidget.setHorizontalHeaderLabels(["Id", "Фамилия", "Имя", "Отчество",
                                                    "Пол", "Класс", "Номер",
                                                    "Номера родителей", "Адрес",
                                                    "Email", "Дата рождения"])
        self.tableWidget.setRowCount(0)
        rowPos = self.tableWidget.rowCount()
        info = ["1", "Гайдомак", "Мария", "Олеговна", "Ж",
                "9а", "89050342142",
                "896576578435", "ул. Краснодарская 11",
                "mary.gaidomak@gmail.com", "13-08-2002"]
        self.add_row(rowPos, info)

        self.class_num_lock = QtWidgets.QLabel(self.class_decr)
        self.class_num_lock.setGeometry(QtCore.QRect(40, 30, 71, 16))
        self.class_num_lock.setFont(font_verdana_12)

        self.layoutWidget = QtWidgets.QWidget(self.class_decr)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 60, 541, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(15)

        self.add_button = white_button(self.class_decr)
        self.add_button.clicked.connect(self.add_new_row)
        self.horizontalLayout.addWidget(self.add_button)

        self.save_button = white_button(self.class_decr)
        self.save_button.clicked.connect(lambda: self.save_row(colCount = colCount))
        self.horizontalLayout.addWidget(self.save_button)

        self.refresh_button = white_button(self.layoutWidget)
        self.horizontalLayout.addWidget(self.refresh_button)



        self.info_about_class_label = QtWidgets.QLabel(self.class_decr)
        self.info_about_class_label.setGeometry(QtCore.QRect(41, 20, 161, 31))
        self.info_about_class_label.setText("Класс: ")

        self.class_num_label = QtWidgets.QLabel(self.class_decr)
        self.class_num_label.setGeometry(QtCore.QRect(110, 30, 71, 16))
        self.class_num_label.setFont(font_verdana_12)
        self.class_num_label.setText("-")

        self.info_about_class_label.setFont(font_verdana_12)

        self.tabWidget.addTab(self.class_decr, "")

        self.document = QtWidgets.QWidget()

        self.review_info_lock = QtWidgets.QLabel(self.document)
        self.review_info_lock.setGeometry(QtCore.QRect(30, 20, 411, 16))
        font_verdana_12.setBold(True)
        self.review_info_lock.setFont(font_verdana_12)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.list_of_pup = QtWidgets.QComboBox(self.document)
        self.list_of_pup.setGeometry(QtCore.QRect(220, 110, 200, 25))
        self.list_of_pup.setFont(font)
        self.list_of_pup.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.list_of_pup.addItem("Item1")
        self.list_of_pup.addItem("Item2")
        self.list_of_pup.addItem("Item3")

        self.enter_id_lock = QtWidgets.QLabel(self.document)
        self.enter_id_lock.setGeometry(QtCore.QRect(30, 105, 191, 31))
        font_verdana_12.setBold(False)
        self.enter_id_lock.setFont(font_verdana_12)

        self.pup_rev_year = white_button(self.document)
        self.pup_rev_year.setGeometry(QtCore.QRect(30, 150, 111, 31))

        self.pup_rev_first = white_button(self.document)
        self.pup_rev_first.setGeometry(QtCore.QRect(150, 150, 171, 31))

        self.pup_rev_second = white_button(self.document)
        self.pup_rev_second.setGeometry(QtCore.QRect(330, 150, 171, 31))

        self.pup_rev_third = white_button(self.document)
        self.pup_rev_third.setGeometry(QtCore.QRect(510, 150, 171, 31))

        self.class_rev_year = white_button(self.document)
        self.class_rev_year.setGeometry(QtCore.QRect(30, 250, 111, 31))

        self.class_rev_second = white_button(self.document)
        self.class_rev_second.setGeometry(QtCore.QRect(330, 250, 171, 31))

        self.get_review_class_lock = QtWidgets.QLabel(self.document)
        self.get_review_class_lock.setGeometry(QtCore.QRect(30, 210, 301, 31))
        self.get_review_class_lock.setFont(font_verdana_12)

        self.class_rev_third = white_button(self.document)
        self.class_rev_third.setGeometry(QtCore.QRect(510, 250, 171, 31))

        self.class_rev_first = white_button(self.document)
        self.class_rev_first.setGeometry(QtCore.QRect(150, 250, 171, 31))

        self.get_review_pup_lock = QtWidgets.QLabel(self.document)
        self.get_review_pup_lock.setGeometry(QtCore.QRect(30, 60, 301, 31))
        self.get_review_pup_lock.setFont(font_verdana_12)

        self.check_table = QtWidgets.QTableWidget(self.document)
        self.check_table.setGeometry(QtCore.QRect(30, 330, 911, 251))
        self.check_table.setObjectName("check_table")
        self.check_table.setColumnCount(0)
        self.check_table.setRowCount(0)

        self.check_label = QtWidgets.QLabel(self.document)
        self.check_label.setGeometry(QtCore.QRect(30, 310, 161, 16))
        self.check_label.setFont(font_verdana_12)
        self.check_label.setText("Просмотр: ")


        self.tabWidget.addTab(self.document, "")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Классное руководство")
        self.label_info_about_teacher_lock.setText("Информация о классном руководителе")
        self.surname_label_lock.setText("Фамилия")
        self.name_label_lock.setText("Имя")
        self.patronymic_label_lock.setText("Отчество")
        self.email_label_lock.setText("Email")
        self.phone_label_lock.setText("Номер")
        self.class_label_lock.setText("Класс")
        self.surname_label.setText("-")
        self.name_label.setText("-")
        self.patronymic_label.setText("-")
        self.email_label.setText("-")
        self.phone_label.setText("-")
        self.class_label.setText("-")
        self.edit_email_lock.setText("Изменить почту")
        self.new_email_lock.setText("Новый email:")
        self.conf_pas_lock.setText("Подтвердите пароль:")
        self.edit_email_button.setText("Изменить email")
        self.new_phone_lock.setText("Новый номер:")
        self.edit_phone_button.setText("Изменить номер")
        self.conf_pass2_lock.setText("Подтвердите пароль:")
        self.edit_phone_lock.setText("Изменить номер телефона")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.profile), "Профиль")
        self.add_button.setText("Добавить ученика")
        self.save_button.setText("Сохранить изменения")
        self.refresh_button.setText("Обновить таблицу")
        self.review_info_lock.setText("Отчет по успеваемости")
        self.enter_id_lock.setText("Выберите ID ученика")
        self.pup_rev_year.setText("Отчет за год")
        self.pup_rev_first.setText("Отчет за 1 триместр")
        self.pup_rev_second.setText("Отчет за 2 триместр")
        self.pup_rev_third.setText("Отчет за 3 триместр")
        self.class_rev_year.setText("Отчет за год")
        self.class_rev_second.setText("Отчет за 2 триместр")
        self.get_review_class_lock.setText("Получить отчет по классу")
        self.class_rev_third.setText("Отчет за 3 триместр")
        self.class_rev_first.setText("Отчет за 1 триместр")
        self.get_review_pup_lock.setText("Получить отчет по ученику")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.class_decr), "Класс")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.document), "Отчёт")

    def add_row(self, current_row, info):
        self.tableWidget.insertRow(current_row)
        for e, i in enumerate(info):
            item = QtWidgets.QTableWidgetItem(i)
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(current_row, e, item)
        self.tableWidget.resizeColumnsToContents()

    def add_new_row(self):
        current_row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(current_row)
        # Поле с id остается не заполненным  - будет автоматически присвоено базой данных
        item = QtWidgets.QTableWidgetItem("")
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(current_row, 0, item)

    def save_row(self, colCount):
        current_row = self.tableWidget.rowCount()
        for i in range(0, current_row):
            print(current_row)
            for l in range(colCount):
                if isinstance(self.tableWidget.item(i,l), QtWidgets.QTableWidgetItem):
                    print(self.tableWidget.item(i, l).text())
                    self.tableWidget.item(i, l).setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.resizeColumnsToContents()



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
