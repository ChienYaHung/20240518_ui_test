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


class HBMainWindow(QWidget):

    # 使用class方法讀取ui檔
    # 方便在class中添加功能

    def __init__(self) -> None:
        super().keyPressEvent(QKeyEvent)
        ui_file_name = "gui-1.ui"  # 設定UI檔案名稱
        ui_file = QFile(ui_file_name)  # 建立用來讀取UI檔的物件

        # 檔案若無法讀取的錯誤訊息
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
            sys.exit(-1)

        # QUiLoader物件可以提供將UI檔內資訊轉換成物件的各種方法
        # QUiLoader需在QApplication之前
        loader = QUiLoader()

        # 建立QApplication物件，管理UI內各種widget
        self.app = QApplication([])

        # 建立物件的ui屬性：
        self.ui = loader.load(ui_file)

        # 結束讀取UI檔
        ui_file.close()

        # 若UI沒有成功建立的錯誤訊息
        if not self.ui:
            print(loader.errorString())
            sys.exit(-1)

        # 建立UI內部參數
        self.gender = '男'
        self.job = self.ui.job_box.currentText()
        self.df_directory = pd.DataFrame(
            columns=['姓名', '性別', '職業', '生日'])  # 資料表

        # 讓日期選擇區顯示今天日期
        self.ui.birthday_input.setDate(QDate.currentDate())

        # slot區
        self.ui.save_data_button.clicked.connect(
            self.save_input_to_directory)  # 儲存資訊至表格
        # 性別選單觸發
        # 選擇時觸發
        self.ui.gender_man.toggled.connect(
            lambda: self.gender_select(self.ui.gender_man))
        self.ui.gender_woman.toggled.connect(
            lambda: self.gender_select(self.ui.gender_woman))
        self.ui.gender_other.toggled.connect(
            lambda: self.gender_select(self.ui.gender_other))
        self.ui.job_box.activated.connect(
            lambda x: self.job_select(x, self.ui.job_box))

    @Slot()
    def save_input_to_directory(self) -> None:
        '''
        儲存通訊錄資訊至表格內
        '''

        # 從輸入區抓取資訊
        human_name = self.ui.name_input.text()
        human_birthday = self.ui.birthday_input.date().toString('yyyy/MM/dd')

        # 檢查姓名是否為空
        if human_name == '':
            self.empty_name_warning_message()
        else:

            # 新增一行
            row_count = self.ui.directory_table.rowCount()
            self.ui.directory_table.insertRow(row_count)

            # 需轉成Item格式
            _human_name = QTableWidgetItem(human_name)
            _human_gender = QTableWidgetItem(f'{self.gender}')
            _human_job = QTableWidgetItem(f'{self.job}')
            _human_birthday = QTableWidgetItem(f'{human_birthday}')

            # 存入dataframe
            _human_data = [human_name, self.gender, self.job, human_birthday]
            self.df_directory.loc[row_count] = _human_data
            self.df_directory.to_clipboard(index=False)

            # 存入表格
            self.ui.directory_table.setItem(row_count, 0, _human_name)
            self.ui.directory_table.setItem(row_count, 1, _human_gender)
            self.ui.directory_table.setItem(row_count, 2, _human_job)
            self.ui.directory_table.setItem(row_count, 3, _human_birthday)
            # self.ui.test_message.setText(f'row: {row_count}')

    # 設定性別
    @Slot()
    def gender_select(self, button) -> None:
        self.gender = button.text()
        # 測試訊息
        self.ui.test_message.setText(f'性別: {self.gender}')

    # 下拉式選單的訊號測試
    @Slot()
    def job_select(self, index, combo_box) -> None:
        self.job = combo_box.currentText()
        # 測試訊息
        self.ui.test_complex_message.setPlainText(f'職業: {self.job}\n第{index}項')

    # 檢查姓名欄是否為空
    def empty_name_warning_message(self):
        msgBox = QMessageBox.warning(
            self.ui, '內容異常', '請輸入姓名', QMessageBox.Ok, QMessageBox.Ok)

    # 鍵盤Ctrl + C複製
    def keyPressEvent(self, event) -> None:
        keycode = event.key()
        # super().keyPressEvent(event)
        self.ui.test_complex_message.setPlainText(str(keycode))
        # 檢查按下按鍵
        # event.key() == Qt.Key.Key_C -> 檢查C鍵
        # event.modifiers() & Qt.KeyboardModifier.ControlModifier -> 檢查Ctrl修飾鍵
        if event.key() == Qt.Key.Key_C and (event.modifiers() & Qt.KeyboardModifier.ControlModifier):
            # selection = self.ui.directory_table.selectedIndexes()
            # self.ui.test_complex_message.setPlainText(
            #     f'複製列index: {selection}')
            self.ui.test_complex_message.setPlainText('Good')


if __name__ == "__main__":

    # 將UI實體化
    hb_window = HBMainWindow()

    # 顯示UI
    hb_window.ui.show()

    # 正常退出APP：app.exec()關閉app
    hb_window.app.exec()
