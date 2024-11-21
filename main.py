import sys
import requests
from PyQt5 import QtCore, QtGui, QtWidgets

class UserManager:
    def __init__(self):
        self.current_login = None
        self.current_user_id = None

    def set_current_login(self, login):
        self.current_login = login

    def get_current_login(self):
        return self.current_login

    def set_current_user_id(self, user_id):
        self.current_user_id = user_id

    def get_current_user_id(self):
        return self.current_user_id

user_manager = UserManager()

class LoginPage(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.register_user)
        self.pushButton_2.clicked.connect(self.login_user)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1148, 783)
        MainWindow.setStyleSheet("background-color: rgb(32, 31, 49);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(400, 240, 301, 61))
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(105, 99, 204);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(400, 320, 301, 61))
        self.lineEdit_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(105, 99, 204);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 1011, 101))
        self.label.setStyleSheet("background-color: rgb(32, 31, 49);\n"
"background-color: rgb(105, 99, 204);\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 140, 301, 81))
        self.label_2.setStyleSheet("background-color: rgb(32, 31, 49);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 1121, 741))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 130, 301, 351))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 390, 131, 81))
        self.pushButton.setStyleSheet("background-color: rgb(105, 99, 204);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 390, 131, 81))
        self.pushButton_2.setStyleSheet("background-color: rgb(105, 99, 204);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1148, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Введите логин"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Введите пароль"))
        self.label.setText(_translate("MainWindow", "                                                                                                                                                     FURNITURE FACTORY"))
        self.label_2.setText(_translate("MainWindow", "                                        Вход на сайт"))
        self.pushButton.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.pushButton_2.setText(_translate("MainWindow", "Авторизироваться"))

    def register_user(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        print(f"Registering user with login: {login}, password: {password}")
        response = requests.post('http://localhost:5000/register', json={'login': login, 'password': password})
        if response.status_code == 201:
            QtWidgets.QMessageBox.information(self, 'Success', 'User registered successfully')
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Failed to register user')

    def login_user(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        print(f"Logging in user with login: {login}, password: {password}")
        response = requests.post('http://localhost:5000/login', json={'login': login, 'password': password})
        if response.status_code == 200:
            data = response.json()
            user_manager.set_current_login(data['login'])
            user_manager.set_current_user_id(data['user_id'])
            QtWidgets.QMessageBox.information(self, 'Success', 'Login successful')
            self.parent().show_main_page()
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Invalid credentials')

class MainPage(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1117, 784)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.glavnayastranica = QtWidgets.QPushButton(self.centralwidget)
        self.glavnayastranica.setGeometry(QtCore.QRect(10, 10, 231, 61))
        self.glavnayastranica.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(105, 99, 204);")
        self.glavnayastranica.setObjectName("glavnayastranica")
        self.corzina = QtWidgets.QPushButton(self.centralwidget)
        self.corzina.setGeometry(QtCore.QRect(600, 10, 241, 61))
        self.corzina.setStyleSheet("background-color: rgb(32, 31, 49);\n"
"color: rgb(255, 255, 255);")
        self.corzina.setObjectName("corzina")
        self.Myaccountuno = QtWidgets.QPushButton(self.centralwidget)
        self.Myaccountuno.setGeometry(QtCore.QRect(860, 10, 231, 61))
        self.Myaccountuno.setStyleSheet("background-color: rgb(32, 31, 49);\n"
"color: rgb(255, 255, 255);")
        self.Myaccountuno.setObjectName("Myaccountuno")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(600, 120, 241, 621))
        self.listWidget.setStyleSheet("background-color: rgb(32, 31, 49);")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(860, 120, 231, 621))
        self.listWidget_2.setStyleSheet("background-color: rgb(32, 31, 49);")
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.listWidget_3 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_3.setGeometry(QtCore.QRect(10, 80, 581, 661))
        self.listWidget_3.setStyleSheet("background-color: rgb(32, 31, 49);")
        self.listWidget_3.setObjectName("listWidget_3")
        self.vidimebeli = QtWidgets.QLabel(self.centralwidget)
        self.vidimebeli.setGeometry(QtCore.QRect(600, 80, 241, 41))
        self.vidimebeli.setStyleSheet("background-color: rgb(105, 99, 204);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(105, 99, 204);")
        self.vidimebeli.setObjectName("vidimebeli")
        self.Proizvoditeli = QtWidgets.QLabel(self.centralwidget)
        self.Proizvoditeli.setGeometry(QtCore.QRect(860, 80, 231, 41))
        self.Proizvoditeli.setStyleSheet("background-color: rgb(105, 99, 204);\n"
"color: rgb(255, 255, 255);")
        self.Proizvoditeli.setObjectName("Proizvoditeli")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1117, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.glavnayastranica.setText(_translate("MainWindow", "Главная"))
        self.corzina.setText(_translate("MainWindow", "Корзина"))
        self.Myaccountuno.setText(_translate("MainWindow", "Мой аккаунт"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Стул"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Кровать"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Диван"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "Кресло"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "Пуфы"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "Шкаф"))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "Комод"))
        item = self.listWidget.item(7)
        item.setText(_translate("MainWindow", "Офисное кресло"))
        item = self.listWidget.item(8)
        item.setText(_translate("MainWindow", "Вешалка"))
        item = self.listWidget.item(9)
        item.setText(_translate("MainWindow", "Колыбель"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MainWindow", "Chairs inc"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("MainWindow", "Tables inc"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("MainWindow", "Bed inc"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("MainWindow", "Couch one"))
        item = self.listWidget_2.item(4)
        item.setText(_translate("MainWindow", "Chair giga inc"))
        item = self.listWidget_2.item(5)
        item.setText(_translate("MainWindow", "Pewpew inc"))
        item = self.listWidget_2.item(6)
        item.setText(_translate("MainWindow", "Clothet inc"))
        item = self.listWidget_2.item(7)
        item.setText(_translate("MainWindow", "Zit inc"))
        item = self.listWidget_2.item(8)
        item.setText(_translate("MainWindow", "HUNGA"))
        item = self.listWidget_2.item(9)
        item.setText(_translate("MainWindow", "Fifa"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.vidimebeli.setText(_translate("MainWindow", "                             Виды мебели"))
        self.Proizvoditeli.setText(_translate("MainWindow", "                        Производители"))

class CartPage(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1108, 651)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.corzina = QtWidgets.QPushButton(self.centralwidget)
        self.corzina.setGeometry(QtCore.QRect(590, 10, 241, 61))
        self.corzina.setStyleSheet("background-color: rgb(32, 31, 49);\n"
"background-color: rgb(105, 99, 204);\n"
"color: rgb(255, 255, 255);")
        self.corzina.setObjectName("corzina")
        self.glavnayastranica = QtWidgets.QPushButton(self.centralwidget)
        self.glavnayastranica.setGeometry(QtCore.QRect(0, 10, 231, 61))
        self.glavnayastranica.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(32, 31, 49);")
        self.glavnayastranica.setObjectName("glavnayastranica")
        self.Myaccountuno = QtWidgets.QPushButton(self.centralwidget)
        self.Myaccountuno.setGeometry(QtCore.QRect(850, 10, 231, 61))
        self.Myaccountuno.setStyleSheet("background-color: rgb(105, 99, 204);\n"
"background-color: rgb(32, 31, 49);\n"
"color: rgb(255, 255, 255);")
        self.Myaccountuno.setObjectName("Myaccountuno")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 80, 551, 531))
        self.label.setStyleSheet("background-color: rgb(32, 31, 49);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(560, 80, 521, 291))
        self.label_2.setStyleSheet("background-color: rgb(32, 31, 49);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(560, 380, 521, 231))
        self.label_3.setStyleSheet("background-color: rgb(32, 31, 49);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.podtverjdenie = QtWidgets.QPushButton(self.centralwidget)
        self.podtverjdenie.setGeometry(QtCore.QRect(710, 300, 221, 61))
        self.podtverjdenie.setObjectName("podtverjdenie")
        self.vveditesvoiadress = QtWidgets.QLineEdit(self.centralwidget)
        self.vveditesvoiadress.setGeometry(QtCore.QRect(570, 90, 501, 61))
        self.vveditesvoiadress.setObjectName("vveditesvoiadress")
        self.vveditekontaktniinomer = QtWidgets.QLineEdit(self.centralwidget)
        self.vveditekontaktniinomer.setGeometry(QtCore.QRect(570, 160, 501, 61))
        self.vveditekontaktniinomer.setObjectName("vveditekontaktniinomer")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(570, 230, 501, 61))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 530, 201, 61))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.oplata = QtWidgets.QPushButton(self.centralwidget)
        self.oplata.setGeometry(QtCore.QRect(350, 530, 191, 61))
        self.oplata.setObjectName("oplata")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(0, 90, 541, 421))
        self.listView.setObjectName("listView")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(570, 390, 501, 211))
        self.listView_2.setObjectName("listView_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1108, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.corzina.setText(_translate("MainWindow", "Корзина"))
        self.glavnayastranica.setText(_translate("MainWindow", "Главная"))
        self.Myaccountuno.setText(_translate("MainWindow", "Мой аккаунт"))
        self.podtverjdenie.setText(_translate("MainWindow", "Подтверждение действия"))
        self.vveditesvoiadress.setPlaceholderText(_translate("MainWindow", "Введите свой адрес"))
        self.vveditekontaktniinomer.setPlaceholderText(_translate("MainWindow", "Введите контактный номер"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Выберите способ оплаты"))
        self.label_4.setText(_translate("MainWindow", "  Итого: "))
        self.oplata.setText(_translate("MainWindow", "Оплатить"))

class AccountPage(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1107, 782)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.glavnayastranica = QtWidgets.QPushButton(self.centralwidget)
        self.glavnayastranica.setGeometry(QtCore.QRect(10, 10, 231, 61))
        self.glavnayastranica.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(32, 31, 49);")
        self.glavnayastranica.setObjectName("glavnayastranica")
        self.Myaccountuno = QtWidgets.QPushButton(self.centralwidget)
        self.Myaccountuno.setGeometry(QtCore.QRect(860, 10, 231, 61))
        self.Myaccountuno.setStyleSheet("background-color: rgb(105, 99, 204);\n"
"color: rgb(255, 255, 255);")
        self.Myaccountuno.setObjectName("Myaccountuno")
        self.corzina = QtWidgets.QPushButton(self.centralwidget)
        self.corzina.setGeometry(QtCore.QRect(600, 10, 241, 61))
        self.corzina.setStyleSheet("background-color: rgb(32, 31, 49);\n"
"color: rgb(255, 255, 255);")
        self.corzina.setObjectName("corzina")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 80, 531, 251))
        self.label.setStyleSheet("background-color: rgb(32, 31, 49);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(560, 80, 531, 361))
        self.label_2.setStyleSheet("background-color: rgb(32, 31, 49);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.vashlogin = QtWidgets.QLabel(self.centralwidget)
        self.vashlogin.setGeometry(QtCore.QRect(20, 90, 511, 71))
        self.vashlogin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.vashlogin.setObjectName("vashlogin")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 511, 71))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 250, 511, 71))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.vvediteparol2 = QtWidgets.QLineEdit(self.centralwidget)
        self.vvediteparol2.setGeometry(QtCore.QRect(570, 90, 511, 71))
        self.vvediteparol2.setObjectName("vvediteparol2")
        self.vveditenoviiperol = QtWidgets.QLineEdit(self.centralwidget)
        self.vveditenoviiperol.setGeometry(QtCore.QRect(570, 170, 511, 71))
        self.vveditenoviiperol.setObjectName("vveditenoviiperol")
        self.podtverditenoviiparol = QtWidgets.QLineEdit(self.centralwidget)
        self.podtverditenoviiparol.setGeometry(QtCore.QRect(570, 250, 511, 71))
        self.podtverditenoviiparol.setObjectName("podtverditenoviiparol")
        self.urverditeparol = QtWidgets.QPushButton(self.centralwidget)
        self.urverditeparol.setGeometry(QtCore.QRect(660, 330, 321, 91))
        self.urverditeparol.setObjectName("urverditeparol")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1107, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.glavnayastranica.setText(_translate("MainWindow", "Главная"))
        self.Myaccountuno.setText(_translate("MainWindow", "Мой аккаунт"))
        self.corzina.setText(_translate("MainWindow", "Корзина"))
        self.vashlogin.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.vvediteparol2.setPlaceholderText(_translate("MainWindow", "Введите нынешний пароль"))
        self.vveditenoviiperol.setPlaceholderText(_translate("MainWindow", "Введите новый пароль "))
        self.podtverditenoviiparol.setPlaceholderText(_translate("MainWindow", "Подтвердите новый пароль"))
        self.urverditeparol.setText(_translate("MainWindow", "Утвердить новый пароль"))

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Furniture Factory")
        self.setGeometry(100, 100, 1148, 783)

        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.login_page = LoginPage()
        self.main_page = MainPage()
        self.cart_page = CartPage()
        self.account_page = AccountPage()

        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.main_page)
        self.stacked_widget.addWidget(self.cart_page)
        self.stacked_widget.addWidget(self.account_page)

        self.stacked_widget.setCurrentWidget(self.login_page)

        self.login_page.pushButton_2.clicked.connect(self.show_main_page)
        self.main_page.Myaccountuno.clicked.connect(self.show_account_page)
        self.main_page.corzina.clicked.connect(self.show_cart_page)
        self.main_page.glavnayastranica.clicked.connect(self.show_main_page)
        self.cart_page.glavnayastranica.clicked.connect(self.show_main_page)
        self.cart_page.Myaccountuno.clicked.connect(self.show_account_page)
        self.cart_page.corzina.clicked.connect(self.show_cart_page)
        self.account_page.glavnayastranica.clicked.connect(self.show_main_page)
        self.account_page.corzina.clicked.connect(self.show_cart_page)
        self.account_page.Myaccountuno.clicked.connect(self.show_account_page)

    def show_main_page(self):
        self.stacked_widget.setCurrentWidget(self.main_page)

    def show_cart_page(self):
        self.stacked_widget.setCurrentWidget(self.cart_page)

    def show_account_page(self):
        self.stacked_widget.setCurrentWidget(self.account_page)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
