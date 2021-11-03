import sys
import pymysql
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets
import csv
import json
import xml.etree.ElementTree as ET

conn = pymysql.connect(host='localhost', user='root', password='tjdals120!', db='kleague', charset='utf8')

cursor = conn.cursor()
sql = "SELECT * FROM player"
cursor.execute(sql)
tuples = cursor.fetchall()

player_num = 0 # 검색문마다 바뀜
column_num = 13 # 고정

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 800)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 560, 64, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 590, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 590, 64, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 590, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 630, 31, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 670, 64, 15))
        self.label_6.setObjectName("label_6")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 720, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 720, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 650, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 911, 511))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(13)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(170, 620, 131, 41))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 10, 57, 19))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(70, 10, 61, 19))
        self.radioButton_2.setObjectName("radioButton_2")

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(170, 660, 131, 41))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 10, 61, 19))
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(70, 10, 61, 19))
        self.radioButton_4.setChecked(False)
        self.radioButton_4.setObjectName("radioButton_4")

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(520, 560, 291, 80))
        self.groupBox_3.setObjectName("groupBox_3")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 40, 71, 19))
        self.radioButton_5.setChecked(False)
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_6.setGeometry(QtCore.QRect(110, 40, 71, 19))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_7.setGeometry(QtCore.QRect(220, 40, 71, 19))
        self.radioButton_7.setObjectName("radioButton_7")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(70, 630, 91, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(70, 670, 91, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(70, 590, 91, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(230, 590, 91, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(390, 590, 91, 22))
        self.comboBox_5.setObjectName("comboBox_5")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 26))
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

        self.groupBox_3.setTitle(_translate("MainWindow", "파일 종류"))

        self.label.setText(_translate("MainWindow", "선수 검색"))
        self.label_2.setText(_translate("MainWindow", "팀명 :"))
        self.label_3.setText(_translate("MainWindow", "포지션 :"))
        self.label_4.setText(_translate("MainWindow", "출신국 :"))
        self.label_5.setText(_translate("MainWindow", "키 : "))
        self.label_6.setText(_translate("MainWindow", "몸무게 : "))

        self.pushButton.setText(_translate("MainWindow", "초기화"))
        self.pushButton_2.setText(_translate("MainWindow", "검색"))
        self.pushButton_3.setText(_translate("MainWindow", "파일 저장"))
        self.pushButton.clicked.connect(self.btn_init_clicked)
        self.pushButton_2.clicked.connect(self.btn_search_clicked)
        self.pushButton_3.clicked.connect(self.btn_save_clicked)

        self.Header = ("PLAYER_ID", "PLAYER_NAME", "TEAM_ID",
                       "E_PLAYER_NAME", "NICKNAME", "JOIN_YYYY",
                       "POSITION", "BACK_NO", "NATION", "BIRTH_DATE",
                       "SOLAR", "HEIGHT", "WEIGHT")
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "PLAYER_ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "PLAYER_NAME"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "TEAM_ID"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "E_PLAYER_NAME"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "NICKNAME"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "JOIN_YYYY"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "POSITION"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "BACK_NO"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "NATION"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "BIRTH_DATE"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "SOLAR"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "HEIGHT"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "WEIGHT"))


        self.radioButton.setText(_translate("MainWindow", "이상"))
        self.radioButton_2.setText(_translate("MainWindow", "이하"))
        self.radioButton_3.setText(_translate("MainWindow", "이상"))
        self.radioButton_4.setText(_translate("MainWindow", "이하"))
        self.radioButton_5.setText(_translate("MainWindow", "CSV"))
        self.radioButton_6.setText(_translate("MainWindow", "JSON"))
        self.radioButton_7.setText(_translate("MainWindow", "XML"))
        self.radioButton.clicked.connect(self.radio_btn_height_more_clicked)
        self.radioButton_2.clicked.connect(self.radio_btn_height_less_clicked)
        self.radioButton_3.clicked.connect(self.radio_btn_weight_more_clicked)
        self.radioButton_4.clicked.connect(self.radio_btn_weight_less_clicked)

        self.team_id = ""
        self.position = ""
        self.nation = ""
        self.players = ""

        sql = "SELECT MIN(height), MAX(height), MIN(weight), MAX(weight) FROM player"
        cursor.execute(sql)
        players = cursor.fetchall()
        min_height = players[0][0]
        max_height = players[0][1]
        min_weight = players[0][2]
        max_weight = players[0][3]
        self.comboBox.addItem("사용안함")
        self.comboBox.currentTextChanged.connect(self.change_height)
        self.height = self.comboBox.currentText()
        self.comboBox_2.addItem("사용안함")
        self.comboBox_2.currentTextChanged.connect(self.change_weight)
        self.weight = self.comboBox_2.currentText()
        for i in range(min_height, max_height + 1):
            self.comboBox.addItem(str(i))
        for j in range(min_weight, max_weight + 1):
            self.comboBox_2.addItem(str(j))

        sql =  "SELECT DISTINCT TEAM_ID FROM player"
        cursor.execute(sql)
        players = cursor.fetchall()
        team_id = players
        self.comboBox_3.addItem("사용안함")
        self.comboBox_3.currentTextChanged.connect(self.change_team_id)
        self.team_id = self.comboBox_3.currentText()
        for i in range(len(team_id)):
            self.comboBox_3.addItem("%s" % players[i])

        sql = "SELECT DISTINCT position FROM player"
        cursor.execute(sql)
        players = cursor.fetchall()
        position = players
        self.comboBox_4.addItem("사용안함")
        self.comboBox_4.currentTextChanged.connect(self.change_position)
        self.position = self.comboBox_4.currentText()
        for i in range(len(position)):
            if i != 2: self.comboBox_4.addItem("%s" % players[i])
        self.comboBox_4.addItem("미정")

        sql = "SELECT DISTINCT NATION FROM player"
        cursor.execute(sql)
        players = cursor.fetchall()
        nation = players
        self.comboBox_5.addItem("사용안함")
        self.comboBox_5.currentTextChanged.connect(self.change_nation)
        self.nation = self.comboBox_5.currentText()
        for i in range(len(nation)):
            if i != 0: self.comboBox_5.addItem("%s" % players[i])
        self.comboBox_5.addItem("대한민국")

    def change_height(self):
        self.height = self.comboBox.currentText()
    def change_weight(self):
        self.weight = self.comboBox_2.currentText()
    def change_team_id(self):
        self.team_id = self.comboBox_3.currentText()
    def change_position(self):
        self.position = self.comboBox_4.currentText()
    def change_nation(self):
        self.nation = self.comboBox_5.currentText()

    def save_CSV(self):
        with open('pyQT_DBAPI.csv', 'w', encoding='utf-8', newline='') as f:
            w = csv.writer(f)
            w.writerow((self.Header))
            for item in self.players:
                w.writerow(item)
    def playersToDict(self):
        data = []
        for i in range(len(self.players)):
            row = {}
            for j in range(len(self.players[i])):
                row[self.Header[j]] = str(self.players[i][j])
            data.append(row)
        return data
    def save_JSON(self):
        data = self.playersToDict()
        for i in range(len(self.players)):
            row = {}
            for j in range(len(self.players[i])):
                row[self.Header[j]] = str(self.players[i][j])
            data.append(row)
        with open('pyQT_DBAPI.json', "w", encoding='utf-8', newline='') as outfile:
            json.dump(data, outfile, ensure_ascii=False)

    def save_XML(self):
        print("!")
        data = self.playersToDict()
        print(data)
        rootElement = ET.Element('Table')
        rootElement.attrib['name'] = 'player'
        for row in data:
            rowElement = ET.Element('Row')
            rootElement.append(rowElement)
            for columnName in list(row.keys()):
                rowElement.attrib[columnName] = str(row[columnName]) if row[columnName] else ''
        ET.ElementTree(rootElement).write("pyQT_DBAPI.xml", encoding='utf-8', xml_declaration=True)

    def btn_save_clicked(self):
        if self.radioButton_5.isChecked():
            self.save_CSV()
        elif self.radioButton_6.isChecked():
            self.save_JSON()
        elif self.radioButton_7.isChecked():
            self.save_XML()

    def radio_btn_height_more_clicked(self):
        self.height = self.comboBox.currentText()

    def radio_btn_height_less_clicked(self):
        self.height = self.comboBox.currentText()

    def radio_btn_weight_more_clicked(self):
        self.weight = self.comboBox_2.currentText()

    def radio_btn_weight_less_clicked(self):
        self.weight = self.comboBox_2.currentText()


    def btn_init_clicked(self):
        self.comboBox.setCurrentText("사용안함")
        self.comboBox_2.setCurrentText("사용안함")
        self.comboBox_3.setCurrentText("사용안함")
        self.comboBox_4.setCurrentText("사용안함")
        self.comboBox_5.setCurrentText("사용안함")
        self.tableWidget.clearContents()

    def btn_search_clicked(self):
        sql = "SELECT * FROM player"
        if self.team_id != "사용안함" or self.position != "사용안함" or self.nation != "사용안함" or self.height != "사용안함" or self.weight != "사용안함":
            sql += " WHERE"
            if (self.team_id != "사용안함") and (self.position != "사용안함" or self.nation != "사용안함" or self.height != "사용안함" or self.weight != "사용안함"):
                sql += " TEAM_ID = '%s' AND " % (self.team_id)
            elif self.team_id != "사용안함":
                sql += " TEAM_ID = '%s'" % (self.team_id)

            if (self.position != "사용안함") and (self.nation != "사용안함" or self.height != "사용안함" or self.weight != "사용안함"):
                sql += " POSITION = '%s' AND" % (self.position)
            elif self.position == "미정" and (self.nation != "사용안함" or self.height != "사용안함" or self.weight != "사용안함"):
                sql += " POSITION = ''%s" % ("IS NULL")
            elif self.position == "미정":
                sql += " POSITION = ''%s" % ("IS NULL")
            elif self.position != "사용안함":
                sql += " POSITION = '%s'" % (self.position)

            if (self.nation != "사용안함" and self.nation != "대한민국") and (self.height != "사용안함" or self.weight != "사용안함"):
                sql += " NATION = '%s' AND" % (self.nation)
            elif self.nation == "대한민국" and (self.height != "사용안함" or self.weight != "사용안함"):
                sql += " NATION = ''%s AND" % ("IS NULL")
            elif self.nation == "대한민국":
                sql += " NATION = ''%s" % ("IS NULL")
            elif self.nation != "사용안함":
                sql += " NATION = '%s'" % (self.nation)

            if self.height != "사용안함" and self.weight != "사용안함":
                if self.radioButton.isChecked():
                    sql += " HEIGHT >= %s AND" % (self.height)
                elif self.radioButton_2.isChecked():
                    sql += " HEIGHT <= %s AND" % (self.height)
            elif self.height != "사용안함":
                if self.radioButton.isChecked():
                    sql += " HEIGHT >= %s " % (self.height)
                elif self.radioButton_2.isChecked():
                    sql += " HEIGHT <= %s " % (self.height)

            if self.weight != "사용안함":
                if self.radioButton_3.isChecked():
                    sql += " WEIGHT >= %s" % (self.weight)
                elif self.radioButton_4.isChecked():
                    sql += " WEIGHT <= %s" % (self.weight)

        cursor.execute(sql)
        players = cursor.fetchall()
        self.players = players
        player_num = len(players)
        self.tableWidget.setRowCount(player_num)

        for i in range(player_num):
            for j in range(column_num):
                temp = players[i][j]
                if (j == 6 and temp == None):  # position
                    temp = "미정"
                elif (j == 8 and temp == None):  # nation
                    temp = "대한민국"
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(temp)))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
