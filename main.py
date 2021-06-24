from PyQt5 import QtWidgets, QtCore
from mysql.connector import connect, Error
import loginWindow
import mainApp
import sys


class TwoWindow(QtWidgets.QMainWindow, mainApp.Ui_MainWindow):
    def __init__(self, personal_data):
        super().__init__()
        self.setupUi(self)
        print(personal_data)
        self.surname_label.setText(personal_data[0][1])
        self.name_label.setText(personal_data[0][2])
        self.patronymic_label.setText(personal_data[0][3])
        self.email_label.setText(personal_data[0][4])
        self.phone_label.setText("+" + personal_data[0][5])
        self.class_label.setText(personal_data[0][6])
        self.class_num_label.setText(personal_data[0][6])
        self.set_table(personal_data[0][6])

    def set_table(self, class_num):
        rowPos = self.tableWidget.rowCount()
        class_data = self.prepare_data(self.get_class_data(class_num))
        print(class_data)
        for i in class_data:
            self.add_row(rowPos, i)
            rowPos = self.tableWidget.rowCount()
            short_pup_info =  i[0] + " | " + i[1] + " " + i[2]+ " " + i[3]
            self.list_of_pup.addItem(short_pup_info)

    def prepare_data(self, data):
        prepared_data = []
        for i in data:
            prepared_data.append(
                [str(i[-1]), i[2], i[3], i[4], i[5], i[1], i[6], i[7], i[8], i[9], str(i[10])]
            )
        prepared_data = sorted(prepared_data, key=self.sort_key)
        return prepared_data

    def sort_key(self, data):
        return data[1]

    def get_class_data(self, class_num):
        data = []
        try:
            with connect(
                    host="db4free.net",
                    user="maria_prog",
                    password="iTBFFA9ymsHh2",
                    port=3306,
                    database="school_bd"
            ) as connection:
                query = """SELECT * FROM pupil_personal_data WHERE class_num = "{}" """.format(class_num)
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    for db in cursor:
                        data.append(db)
                return data
        except Error as e:
            print(e)


class OneWindow(QtWidgets.QMainWindow, loginWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.twoWindow = None
        self.enterbutton.clicked.connect(lambda: self.enter_app(self.loginEdit.text(), self.passwordEdit.text()))

    def enter_app(self, login, password):
        answer, data, personal_data = connect_to_db(login, password)
        if answer:
            print(data)
            # print(personal_data)
            self.info_label.setText("Осуществляем вход")
            self.twoWindow = TwoWindow(personal_data)
            self.twoWindow.show()
            self.close()
        else:
            self.info_label.setText("Неверный логин или пароль")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = OneWindow()
    window.show()
    sys.exit(app.exec_())


def connect_to_db(login, password):
    data = []
    peronal_data = []
    answer = False
    try:
        with connect(
                host="db4free.net",
                user="maria_prog",
                password="iTBFFA9ymsHh2",
                port=3306,
                database="school_bd"
        ) as connection:
            show_db_query = """SELECT * FROM users WHERE login = "{}" """.format(login)
            with connection.cursor() as cursor:
                cursor.execute(show_db_query)
                for db in cursor:
                    data.append(db)
            if len(data) > 0:
                if password == data[0][2]:
                    show_db_query = """SELECT * FROM users_data WHERE id = "{}" """.format(data[0][0])
                    with connection.cursor() as cursor:
                        cursor.execute(show_db_query)
                        for db in cursor:
                            peronal_data.append(db)
                    answer = True
                    return answer, data, peronal_data
                else:
                    return answer, data, peronal_data
    except Error as e:
        print(e)
        return answer, data, peronal_data


if __name__ == "__main__":
    main()
