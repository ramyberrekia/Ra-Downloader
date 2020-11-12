# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(631, 332)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("/*  ---------------------------- ALL OTHERS WIDGETS ---------------------------- */\n"
"*{\n"
"selection-background-color: rgb(67, 128, 179);\n"
"selection-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/*  ---------------------------- MAIN WINDOW, WIDGET ---------------------------- */\n"
"QMainWindow,QWidget\n"
"{\n"
"color:rgb(0,0,0);\n"
"background:rgb(255,255,255);\n"
"}\n"
"\n"
"/*  ---------------------------- MENU BAR ---------------------------- */\n"
"QMenuBar\n"
"{\n"
"color:rgb(120,120,120);\n"
"background:rgb(230,230,230);\n"
"}\n"
"QMenuBar::item:selected\n"
"{\n"
"color:rgb(100,100,100);\n"
"background:rgb(200,200,200);\n"
"}\n"
"/*  ---------------------------- CONTEXT MENU ---------------------------- */\n"
"QMenu\n"
"{\n"
"color:rgb(90,90,90);\n"
"background:rgb(230,230,230);\n"
"padding: 3;\n"
"}\n"
"QMenu::item:selected\n"
"{\n"
"color:rgb(90,90,90);\n"
"background:rgb(200,200,200);\n"
"}\n"
"QMenu::separator {\n"
"background:rgb(200,200,200);\n"
"height:1px;\n"
"}\n"
"\n"
"\n"
"/*  ---------------------------- Q TAB BAR ---------------------------- */\n"
"QTabBar::tab {\n"
"color:rgb(150,150,150);\n"
"background:rgb(240,240,240);\n"
"height:30;\n"
"width:80;\n"
"border: rgb(240,240,240);\n"
"border-width: 0 0 2px 0;\n"
"padding-left:10;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"background:white;\n"
"color:rgb(100,100,100);\n"
"border: solid rgb(0,150,255);\n"
"border-width: 0 0 5px 0;\n"
"}\n"
"QTableWidget QTableCornerButton::section {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"/*-----------------------------------------------------------------\n"
"------------------------------ LINE_EDIT --------------------------\n"
"------------------------------ TEXT BROWSER -----------------------\n"
"------------------------------ TEXT_EDIT---------------------------\n"
"------------------------------ PLAIN_TEXT -------------------------\n"
"------------------------------------------------------------------- */\n"
"QLineEdit,QTextBrowser,QTextEdit,QPlainTextEdit\n"
"{\n"
"color:rgb(20,20,20);\n"
"background-color:white;\n"
"border: solid lightgrey;\n"
"border-width: 0 0 2px 0;\n"
"border-bottom-left-radius: 5;\n"
"border-bottom-right-radius: 5;\n"
"}\n"
"\n"
"QLineEdit:disabled\n"
"{\n"
"color:rgb(160, 150, 150);\n"
"background-color:rgb(255, 240, 240);\n"
"border: solid rgb(253, 14, 14);\n"
"border-width: 0 0 2px 0;\n"
"border-bottom-left-radius: 5;\n"
"border-bottom-right-radius: 5;\n"
"}\n"
"\n"
"/*  ---------------------------- COMBO BOX ----------------------------*/\n"
"QComboBox\n"
"{\n"
"color:rgb(0,115,170);\n"
"background-color:rgb(255, 255, 255);\n"
"min-width: 5px;\n"
"padding: 1px 0px 1px 3px;\n"
"border: 1px solid rgb(0,115,170);\n"
"}\n"
"\n"
"QComboBox:hover\n"
"{\n"
"color:rgb(0,115,170);\n"
"background-color: white;\n"
"}\n"
"\n"
"QComboBox:selected\n"
"{\n"
"color:rgb(0,115,170);\n"
"selection-background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"width: 30px;\n"
"background-color:rgb(0,115,170);\n"
"}\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(assets/UI/Icons/interface_icons/arrow_down.png);\n"
"width: 14px;\n"
"height: 14px;\n"
"}\n"
"\n"
"\n"
"/* -------------------------------- CHECK BOX ----------------------------------------- */\n"
"QCheckBox\n"
"{\n"
"background: rgb(255, 255, 255);\n"
"color:rgb(25, 29, 32);\n"
"padding: 6;\n"
"}\n"
"/* ----------------------------  TOOL BOX  ----------------------------  */\n"
"QToolBox::tab\n"
"{\n"
"color:darkgrey;\n"
"background:lightgrey;\n"
"}\n"
"QToolBox::tab::selected\n"
"{\n"
"color:grey;\n"
"background:rgb(250, 250,250);\n"
"}\n"
"QToolBox::tab::hover\n"
"{\n"
"color:white;\n"
"background:rgb(0,115,170);\n"
"}\n"
"/*  ---------------------------- PROGRESS BAR ---------------------------- */\n"
"QProgressBar {\n"
"color:grey;\n"
"text-align: center;\n"
"font-size:13px;\n"
"}\n"
"QProgressBar::chunk {\n"
"background:rgb(0, 193, 50);\n"
"}\n"
"/*  ---------------------------- PUSHBUTTON ---------------------------- */\n"
"QPushButton\n"
"{\n"
"border: 1px solid lightgrey;\n"
"color:white;\n"
"background:rgb(0,115,170);\n"
"min-height:30;\n"
"min-width: 50;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border: 1px solid lightgrey;\n"
"color:white;\n"
"background:rgb(0, 120, 210);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"border: 1px solid lightgrey;\n"
"color:white;\n"
"background:rgb(0, 53, 100);\n"
"}\n"
"/*  ----------------------------  LCD NUMBER ---------------------------- */\n"
"QLCDNumber\n"
"{\n"
"color:rgb(0,115,170);\n"
"border:2 solid rgb(100,100,100);\n"
"}\n"
"/*  ---------------------------- TABLE_LIST_TABLE ---------------------------- */\n"
"QTableView,\n"
"QTableWidget\n"
"{\n"
"alternate-background-color: rgb(240, 250, 255);\n"
"}\n"
"QTreeView\n"
"{\n"
"background: rgb(250,250,250);\n"
"color: rgb(180,180,180);\n"
"}\n"
"QTableView::item:selected, \n"
"QListView::item:selected,\n"
"QTableView::item:hover, \n"
"QListView::item:hover, \n"
"QTreeView::item:hover\n"
"{\n"
"background:rgb(0,115,170);\n"
"color:rgb(250,250,250);\n"
"}\n"
"QTableView::item, \n"
"QListView::item, \n"
"QTreeView::item\n"
"{\n"
"color:rgb(100,100,100);\n"
"}\n"
"QTreeView::item:selected,QListView::item:selected,QTableView::item:selected\n"
"{\n"
"color:rgb(37, 62, 71);\n"
"background:rgb(209, 241, 252);\n"
"}\n"
"/* QTreeView::item:has-children\n"
"{\n"
"background-color: rgb(0, 78, 134);\n"
"color: white;\n"
"border-bottom: 2px solid qlineargradient(spread:pad, x1:1, y1:0.5, x2:0, y2:0.5, stop:0 rgba(255, 255, 255, 0), stop:0.5 rgba(0, 150, 255, 255), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"*/\n"
"/*  ---------------------------- HEADER VIEW ---------------------------- */\n"
"QHeaderView::section\n"
"{\n"
"color:rgb(133, 133, 133);\n"
"background:white;\n"
"border:transparent;\n"
"text-align:center;\n"
"padding:1;\n"
"}\n"
"/* ------------------------------- CALENDAR -------------------------------------------------- */\n"
"QCalendarView\n"
"{\n"
"color: rgb(20,20,20);\n"
"background-color: rgb(240,240,240);\n"
"alternate-background-color: rgb(0,115,170);\n"
"selection-background-color: white;\n"
"selection-color: black;\n"
"}\n"
"QAbstractItemView\n"
"{\n"
"color:rgb(200,200,200);\n"
"}\n"
"\n"
"\n"
"/* ---------------------------------------- SLIDER HORIZONTAL ----------------------------------------------- */\n"
"\n"
"\n"
"QSlider::groove:horizontal,QSlider::add-page:horizontal\n"
"{\n"
"background: rgb(255, 255, 255);\n"
"height: 27px;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"height: 10px;\n"
"background: rgb(0,115,170);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"margin-right: -10px;\n"
"margin-left: -10px;\n"
"background: rgb(0,115,170);\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"background:rgb(0,115,170);\n"
"}\n"
"\n"
"/* --------------------------------  VERTICAL SLIDER --------------------------------------------------------------  */\n"
"\n"
"QSlider::handle\n"
"{\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::groove:vertical,QSlider::add-page:vertical,QSlider::sub-page:vertical\n"
"{\n"
"width: 20px;\n"
"background: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"margin-top: -10px;\n"
"margin-bottom: -10px;\n"
"background: rgb(0,115,170);\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"background: rgb(0,115,170);\n"
"}\n"
"\n"
"/* --------------------------------- SCROLLBAR HORIZONTAL --------------------------------------  */\n"
"\n"
"QScrollBar::groove:horizontal{\n"
"background: white;\n"
"height: 17px;\n"
"}\n"
"QScrollBar::sub-page:horizontal,QScrollBar::add-page:horizontal  {\n"
"height: 10px;\n"
"background: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"margin-right: -5px;\n"
"background: rgb(0,115,170);\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"background: rgb(0,115,170);\n"
"}\n"
"\n"
"/* --------------------------------------- SCROLLBAR VERTICAL ----------------------------------------------  */\n"
"\n"
"/* SCROLLBAR */\n"
"QScrollBar:vertical {\n"
"background: white;\n"
"width: 15px;\n"
"margin: 22px 0 22px 0;\n"
"}\n"
"/* HANDLE*/\n"
"QScrollBar::handle:vertical {\n"
"background: rgb(0,115,170);\n"
"min-height: 20px;\n"
"}\n"
"\n"
"/* UP ARROW */\n"
"QScrollBar::up-arrow:vertical {\n"
"image: url(assets/UI/Icons/interface_icons/arrow_up.png);\n"
"width: 10px;\n"
"height: 10px;\n"
"}\n"
"/* DOWN ARROW */\n"
"QScrollBar::down-arrow:vertical {\n"
"image: url(assets/UI/Icons/interface_icons/arrow_down.png);\n"
"width: 10px;\n"
"height: 10px;\n"
"}\n"
"/* UP BUTTON */\n"
"QScrollBar::sub-line:vertical {\n"
"background: rgb(0,115,170);\n"
"height: 20px;\n"
"subcontrol-position: top;\n"
"subcontrol-origin: margin;\n"
"}\n"
"/* DOWN BUTTON */\n"
"QScrollBar::add-line:vertical {\n"
"background: rgb(0,115,170);\n"
"height: 20px;\n"
"subcontrol-position: bottom;\n"
"subcontrol-origin: margin;\n"
"}\n"
"/* SUBPAGES - ADDPAGE */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"background: none;\n"
"}\n"
"/* ---------------------------------- Q TOOL BAR -------------------------------------------------------- */\n"
"/* TOOLBAR REGION */\n"
"QToolBar {\n"
"background: rgb(35,40,45);\n"
"spacing: 20;\n"
"\n"
"}\n"
"/* SEPARATOR */\n"
"QToolBar:separator\n"
"{\n"
"background: rgb(80, 80, 80);\n"
"height: 2;\n"
"}\n"
"/* QToolBar QToolButton { \n"
"    width: 100px;\n"
"} */\n"
"/* -----------------------------------------------Q TOOL BUTTON------------------------------------------- */\n"
"/* BUTTON */\n"
"QToolButton\n"
"{\n"
"color: rgb(255, 255, 255);\n"
"background:rgb(35,40,45);\n"
"}\n"
"\n"
"QToolButton:hover,QToolButton:pressed\n"
"{\n"
"background-color: rgb(64, 73, 82);\n"
"}\n"
"\n"
"QMessageBox QLabel\n"
"{\n"
"color: red;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 631, 301))
        self.tabWidget.setMaximumSize(QtCore.QSize(631, 301))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 60, 101, 21))
        self.label.setStyleSheet("font-size: 15;")
        self.label.setObjectName("label")
        self.BrowseButton = QtWidgets.QPushButton(self.tab)
        self.BrowseButton.setGeometry(QtCore.QRect(530, 100, 88, 34))
        self.BrowseButton.setStyleSheet("font-size: 15px;\n"
"padding-top: 2px;")
        self.BrowseButton.setObjectName("BrowseButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 60, 461, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.DowloadButton = QtWidgets.QPushButton(self.tab)
        self.DowloadButton.setGeometry(QtCore.QRect(260, 190, 141, 34))
        self.DowloadButton.setStyleSheet("padding-top:2px;")
        self.DowloadButton.setObjectName("DowloadButton")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 111, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(190, 10, 311, 21))
        self.label_3.setStyleSheet("\n"
"font: 8pt \"8514oem\";")
        self.label_3.setObjectName("label_3")
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(220, 150, 221, 23))
        self.progressBar.setMinimumSize(QtCore.QSize(0, 23))
        self.progressBar.setStyleSheet("")
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(130, 100, 391, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 101, 21))
        self.label_4.setStyleSheet("font-size: 15;")
        self.label_4.setObjectName("label_4")
        self.BrowseButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.BrowseButton_2.setGeometry(QtCore.QRect(530, 80, 88, 34))
        self.BrowseButton_2.setStyleSheet("font-size: 15px;\n"
"padding-top: 2px;")
        self.BrowseButton_2.setObjectName("BrowseButton_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 40, 391, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.DowloadButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.DowloadButton_2.setGeometry(QtCore.QRect(260, 160, 141, 34))
        self.DowloadButton_2.setStyleSheet("padding-top:2px;")
        self.DowloadButton_2.setObjectName("DowloadButton_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(20, 80, 111, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(150, 10, 381, 21))
        self.label_6.setStyleSheet("\n"
"font: 8pt \"8514oem\";")
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 80, 391, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(20, 120, 111, 21))
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(130, 120, 321, 22))
        self.comboBox.setObjectName("comboBox")
        self.BrowseButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.BrowseButton_4.setGeometry(QtCore.QRect(530, 40, 88, 34))
        self.BrowseButton_4.setStyleSheet("font-size: 9px;\n"
"padding-top: 2px;")
        self.BrowseButton_4.setObjectName("BrowseButton_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(20, 40, 101, 21))
        self.label_8.setStyleSheet("font-size: 15;")
        self.label_8.setObjectName("label_8")
        self.BrowseButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.BrowseButton_3.setGeometry(QtCore.QRect(530, 80, 88, 34))
        self.BrowseButton_3.setStyleSheet("font-size: 15px;\n"
"padding-top: 2px;")
        self.BrowseButton_3.setObjectName("BrowseButton_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 40, 461, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.DowloadButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.DowloadButton_3.setGeometry(QtCore.QRect(260, 140, 141, 34))
        self.DowloadButton_3.setStyleSheet("padding-top:2px;")
        self.DowloadButton_3.setObjectName("DowloadButton_3")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(20, 80, 111, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(130, 10, 411, 21))
        self.label_10.setStyleSheet("\n"
"font: 8pt \"8514oem\";")
        self.label_10.setObjectName("label_10")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(130, 80, 391, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 631, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "File URL:"))
        self.BrowseButton.setText(_translate("MainWindow", "Browse"))
        self.DowloadButton.setText(_translate("MainWindow", "Download"))
        self.label_2.setText(_translate("MainWindow", "Save location:"))
        self.label_3.setText(_translate("MainWindow", "Welcome to files downloader."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Files Downloader"))
        self.label_4.setText(_translate("MainWindow", "File URL:"))
        self.BrowseButton_2.setText(_translate("MainWindow", "Browse"))
        self.DowloadButton_2.setText(_translate("MainWindow", "Download"))
        self.label_5.setText(_translate("MainWindow", "Save location:"))
        self.label_6.setText(_translate("MainWindow", "Welcome to Youtube videos downloader."))
        self.label_7.setText(_translate("MainWindow", "Video quality:"))
        self.BrowseButton_4.setText(_translate("MainWindow", "Get Video Quality"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Vid Downloader"))
        self.label_8.setText(_translate("MainWindow", "File URL:"))
        self.BrowseButton_3.setText(_translate("MainWindow", "Browse"))
        self.DowloadButton_3.setText(_translate("MainWindow", "Download"))
        self.label_9.setText(_translate("MainWindow", "Save location:"))
        self.label_10.setText(_translate("MainWindow", "Welcome to Youtube playlists downloader."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Playlists Downloader"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))