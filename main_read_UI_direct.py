import sys
from PySide6 import QtCore
from PySide6.QtUiTools import QUiLoader
# from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
#                             QMetaObject, QObject, QPoint, QRect,
#                             QSize, QTime, QUrl, Qt, QFile, QIODevice)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform, QColor, QFont)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
                               QHBoxLayout, QHeaderView, QLabel, QLineEdit,
                               QMainWindow, QMenuBar, QPushButton, QRadioButton,
                               QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
                               QTableWidgetItem, QVBoxLayout, QWidget)


class HBMainWindow:

    # 使用class方法讀取ui檔
    # 方便在class中添加功能

    def __init__(self) -> None:

        ui_file_name = "gui-1.ui"  # 設定UI檔案名稱
        ui_file = QtCore.QFile(ui_file_name)  # 建立用來讀取UI檔的物件

        # 檔案若無法讀取的錯誤訊息
        if not ui_file.open(QtCore.QIODevice.ReadOnly):
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

        self.gender = '男'

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

    @QtCore.Slot()
    def save_input_to_directory(self) -> None:
        '''
        儲存通訊錄資訊至表格內
        '''

        # 新增一行
        row_count = self.ui.directory_table.rowCount()
        self.ui.directory_table.insertRow(row_count)

        # 從輸入區抓取資訊
        human_name = self.ui.name_input.text()
        human_job = self.ui.job_box.currentText()
        # 需轉成Item格式
        _human_name = QTableWidgetItem(human_name)
        _human_gender = QTableWidgetItem(f'{self.gender}')
        _human_job = QTableWidgetItem(f'{human_job}')
        # _human_date = QTableWidgetItem(f'{human_name}')

        # 存入表格
        self.ui.directory_table.setItem(row_count, 0, _human_name)
        self.ui.directory_table.setItem(row_count, 1, _human_gender)
        self.ui.directory_table.setItem(row_count, 2, _human_job)
        # self.ui.test_message.setText(f'row: {row_count}')

    # 設定性別
    def gender_select(self, button) -> None:
        self.gender = button.text()
        self.ui.test_message.setText(f'性別: {self.gender}')


if __name__ == "__main__":

    # 將UI實體化
    hb_window = HBMainWindow()

    # 顯示UI
    hb_window.ui.show()

    # 正常退出APP：app.exec()關閉app
    hb_window.app.exec()
