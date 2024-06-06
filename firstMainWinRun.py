# -*- coding: utf-8 -*-
import sys

from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import pandas as pd
# from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
#                             QMetaObject, QObject, QPoint, QRect,
#                             QSize, QTime, QUrl, Qt, QFile, QIODevice)
# from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
#                            QFont, QFontDatabase, QGradient, QIcon,
#                            QImage, QKeySequence, QLinearGradient, QPainter,
#                            QPalette, QPixmap, QRadialGradient, QTransform, QColor, QFont)
# from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
#                                QHBoxLayout, QHeaderView, QLabel, QLineEdit,
#                                QMainWindow, QMenuBar, QPushButton, QRadioButton,
#                                QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
#                                QTableWidgetItem, QVBoxLayout, QWidget, QMessageBox)
from mainUI import *


class MyMainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        # 建立UI內部參數
        self.gender = '男'
        self.job = self.job_box.currentText()
        self.df_directory = pd.DataFrame(
            columns=['姓名', '性別', '職業', '生日'])  # 資料表

        # 讓日期選擇區顯示今天日期
        self.birthday_input.setDate(QDate.currentDate())

        # slot區
        self.save_data_button.clicked.connect(
            self.save_input_to_directory)  # 儲存資訊至表格
        # 性別選單觸發
        # 選擇時觸發
        self.gender_man.toggled.connect(
            lambda: self.gender_select(self.gender_man))
        self.gender_woman.toggled.connect(
            lambda: self.gender_select(self.gender_woman))
        self.gender_other.toggled.connect(
            lambda: self.gender_select(self.gender_other))
        self.job_box.activated.connect(
            lambda x: self.job_select(x, self.job_box))

    @Slot()
    def save_input_to_directory(self) -> None:
        '''
        儲存通訊錄資訊至表格內
        '''

        # 從輸入區抓取資訊
        human_name = self.name_input.text()
        human_birthday = self.birthday_input.date().toString('yyyy/MM/dd')

        # 檢查姓名是否為空
        if human_name == '':
            self.empty_name_warning_message()
        else:

            # 新增一行
            row_count = self.directory_table.rowCount()
            self.directory_table.insertRow(row_count)

            # 需轉成Item格式
            _human_name = QTableWidgetItem(human_name)
            _human_gender = QTableWidgetItem(f'{self.gender}')
            _human_job = QTableWidgetItem(f'{self.job}')
            _human_birthday = QTableWidgetItem(f'{human_birthday}')

            # 存入dataframe
            _human_data = [human_name, self.gender, self.job, human_birthday]
            self.df_directory.loc[row_count] = _human_data
            # self.df_directory.to_clipboard(index=False)

            # 存入表格
            self.directory_table.setItem(row_count, 0, _human_name)
            self.directory_table.setItem(row_count, 1, _human_gender)
            self.directory_table.setItem(row_count, 2, _human_job)
            self.directory_table.setItem(row_count, 3, _human_birthday)
            # self.test_message.setText(f'row: {row_count}')

    # 設定性別
    @Slot()
    def gender_select(self, button) -> None:
        self.gender = button.text()
        # 測試訊息
        # self.test_message.setText(f'性別: {self.gender}')

    # 下拉式選單的訊號測試
    @Slot()
    def job_select(self, index, combo_box) -> None:
        self.job = combo_box.currentText()
        # 測試訊息
        # self.test_complex_message.setPlainText(f'職業: {self.job}\n第{index}項')

    # 檢查姓名欄是否為空
    def empty_name_warning_message(self):
        msgBox = QMessageBox.warning(
            self, '內容異常', '請輸入姓名', QMessageBox.Ok, QMessageBox.Ok)

    # 鍵盤Ctrl + C複製
    def keyPressEvent(self, event) -> None:
        super().keyPressEvent(event)

        # 檢查按下按鍵
        # event.key() == Qt.Key.Key_C -> 檢查C鍵
        # event.modifiers() & Qt.KeyboardModifier.ControlModifier -> 檢查Ctrl修飾鍵
        if event.key() == Qt.Key.Key_C and (event.modifiers() & Qt.KeyboardModifier.ControlModifier):

            # 取得選取列資訊
            # 回傳QTableWidgetItem的list
            selection = self.directory_table.selectedIndexes()
            # QTableWidgetItem取出row index
            selected_row_list = [row_index.row() for row_index in selection]

            # 從dataframe複製指定row至clipboard
            df_directory_copy = self.df_directory.iloc[selected_row_list]
            df_directory_copy.to_clipboard(index=False)

            # 測試訊息
            # self.test_complex_message.setPlainText(f'複製列index: {selection}')
            # self.test_message.setText(f'Type: {selected_row_list}')
            # self.test_complex_message.setPlainText('Good')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec())
