# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui-1.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 450)
        MainWindow.setMinimumSize(QSize(1000, 450))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 30, 941, 361))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setIndent(0)

        self.verticalLayout.addWidget(self.label_2)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.name_input = QLineEdit(self.horizontalLayoutWidget)
        self.name_input.setObjectName(u"name_input")

        self.verticalLayout_2.addWidget(self.name_input)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gender_man = QRadioButton(self.horizontalLayoutWidget)
        self.gender_man.setObjectName(u"gender_man")
        self.gender_man.setChecked(True)

        self.horizontalLayout.addWidget(self.gender_man)

        self.gender_woman = QRadioButton(self.horizontalLayoutWidget)
        self.gender_woman.setObjectName(u"gender_woman")

        self.horizontalLayout.addWidget(self.gender_woman)

        self.gender_other = QRadioButton(self.horizontalLayoutWidget)
        self.gender_other.setObjectName(u"gender_other")

        self.horizontalLayout.addWidget(self.gender_other)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.job_box = QComboBox(self.horizontalLayoutWidget)
        self.job_box.addItem("")
        self.job_box.addItem("")
        self.job_box.addItem("")
        self.job_box.addItem("")
        self.job_box.addItem("")
        self.job_box.addItem("")
        self.job_box.setObjectName(u"job_box")

        self.horizontalLayout_2.addWidget(self.job_box)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.dateEdit = QDateEdit(self.horizontalLayoutWidget)
        self.dateEdit.setObjectName(u"dateEdit")

        self.verticalLayout_2.addWidget(self.dateEdit)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.line = QFrame(self.horizontalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.horizontalSpacer_2 = QSpacerItem(110, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.save_data_button = QPushButton(self.horizontalLayoutWidget)
        self.save_data_button.setObjectName(u"save_data_button")
        self.save_data_button.setFont(font)

        self.verticalLayout_3.addWidget(self.save_data_button)

        self.remove_data_Button = QPushButton(self.horizontalLayoutWidget)
        self.remove_data_Button.setObjectName(u"remove_data_Button")
        self.remove_data_Button.setFont(font)

        self.verticalLayout_3.addWidget(self.remove_data_Button)

        self.save_xlsx_button = QPushButton(self.horizontalLayoutWidget)
        self.save_xlsx_button.setObjectName(u"save_xlsx_button")
        self.save_xlsx_button.setFont(font)

        self.verticalLayout_3.addWidget(self.save_xlsx_button)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.directory_table = QTableWidget(self.horizontalLayoutWidget)
        if (self.directory_table.columnCount() < 4):
            self.directory_table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.directory_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.directory_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.directory_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.directory_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.directory_table.setObjectName(u"directory_table")
        self.directory_table.setRowCount(0)

        self.verticalLayout_4.addWidget(self.directory_table)

        self.line_2 = QFrame(self.horizontalLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_2)

        self.test_message = QLineEdit(self.horizontalLayoutWidget)
        self.test_message.setObjectName(u"test_message")

        self.verticalLayout_4.addWidget(self.test_message)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.line_3 = QFrame(self.horizontalLayoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_5.addWidget(self.label_5)

        self.test_complex_message = QPlainTextEdit(self.horizontalLayoutWidget)
        self.test_complex_message.setObjectName(u"test_complex_message")

        self.verticalLayout_5.addWidget(self.test_complex_message)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d\uff1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6027\u5225\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u8077\u696d\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u751f\u65e5\uff1a", None))
        self.gender_man.setText(QCoreApplication.translate("MainWindow", u"\u7537", None))
        self.gender_woman.setText(QCoreApplication.translate("MainWindow", u"\u5973", None))
        self.gender_other.setText(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6", None))
        self.job_box.setItemText(0, QCoreApplication.translate("MainWindow", u"\u58eb", None))
        self.job_box.setItemText(1, QCoreApplication.translate("MainWindow", u"\u8fb2", None))
        self.job_box.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5de5", None))
        self.job_box.setItemText(3, QCoreApplication.translate("MainWindow", u"\u5546", None))
        self.job_box.setItemText(4, QCoreApplication.translate("MainWindow", u"\u5b78\u751f", None))
        self.job_box.setItemText(5, QCoreApplication.translate("MainWindow", u"\u5c3c\u7279", None))

        self.save_data_button.setText(QCoreApplication.translate("MainWindow", u"\u5132\u5b58\u8f38\u5165\u8cc7\u8a0a", None))
        self.remove_data_Button.setText(QCoreApplication.translate("MainWindow", u"\u522a\u9664\u6240\u9078\u8cc7\u6599", None))
        self.save_xlsx_button.setText(QCoreApplication.translate("MainWindow", u"\u8f38\u51faxlsx\u6a94", None))
        ___qtablewidgetitem = self.directory_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None));
        ___qtablewidgetitem1 = self.directory_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u6027\u5225", None));
        ___qtablewidgetitem2 = self.directory_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u8077\u696d", None));
        ___qtablewidgetitem3 = self.directory_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u751f\u65e5", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6e2c\u8a66\u8a0a\u606f2", None))
    # retranslateUi

