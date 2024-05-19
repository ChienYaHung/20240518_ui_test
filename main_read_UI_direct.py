import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtGui import QColor, QFont


class HBMainWindow:

    # 使用class方法讀取ui檔
    # 方便在class中添加功能

    def __init__(self) -> None:

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

        # slot區
        # 按鍵動作測試
        self.ui.save_data_button.clicked.connect(self.say_hello)

    def say_hello(self):
        font = QFont()
        font.setPointSize(14)
        self.ui.input_display.setPlainText('Hello world!\nRun correctly')


if __name__ == "__main__":

    # 將UI實體化
    hb_window = HBMainWindow()

    # 顯示UI
    hb_window.ui.show()

    # 正常退出APP：app.exec()關閉app
    hb_window.app.exec()
