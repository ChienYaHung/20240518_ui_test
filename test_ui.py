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
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 30, 621, 141))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setIndent(0)

        self.verticalLayout.addWidget(self.label_2)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.name_input = QLineEdit(self.widget)
        self.name_input.setObjectName(u"name_input")

        self.verticalLayout_2.addWidget(self.name_input)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gender_man = QRadioButton(self.widget)
        self.gender_man.setObjectName(u"gender_man")

        self.horizontalLayout.addWidget(self.gender_man)

        self.gander_woman = QRadioButton(self.widget)
        self.gander_woman.setObjectName(u"gander_woman")

        self.horizontalLayout.addWidget(self.gander_woman)

        self.gender_other = QRadioButton(self.widget)
        self.gender_other.setObjectName(u"gender_other")

        self.horizontalLayout.addWidget(self.gender_other)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.dateEdit = QDateEdit(self.widget)
        self.dateEdit.setObjectName(u"dateEdit")

        self.verticalLayout_2.addWidget(self.dateEdit)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.horizontalSpacer_2 = QSpacerItem(220, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.save_data_button = QPushButton(self.widget)
        self.save_data_button.setObjectName(u"save_data_button")
        self.save_data_button.setFont(font)

        self.verticalLayout_3.addWidget(self.save_data_button)

        self.clear_data_button = QPushButton(self.widget)
        self.clear_data_button.setObjectName(u"clear_data_button")
        self.clear_data_button.setFont(font)

        self.verticalLayout_3.addWidget(self.clear_data_button)

        self.remove_data_Button = QPushButton(self.widget)
        self.remove_data_Button.setObjectName(u"remove_data_Button")
        self.remove_data_Button.setFont(font)

        self.verticalLayout_3.addWidget(self.remove_data_Button)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
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
        self.gander_woman.setText(QCoreApplication.translate("MainWindow", u"\u5973", None))
        self.gender_other.setText(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u58eb", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u8fb2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5de5", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u5546", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u5b78\u751f", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"\u5c3c\u7279", None))

        self.save_data_button.setText(QCoreApplication.translate("MainWindow", u"\u5132\u5b58\u8f38\u5165\u8cc7\u8a0a", None))
        self.clear_data_button.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u8f38\u5165\u8cc7\u8a0a", None))
        self.remove_data_Button.setText(QCoreApplication.translate("MainWindow", u"\u522a\u9664\u6240\u9078\u8cc7\u6599", None))
    # retranslateUi

