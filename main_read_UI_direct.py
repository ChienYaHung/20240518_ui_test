import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtGui import QColor, QFont


class HBMainWindow:
    def __init__(self) -> None:
        ui_file_name = "gui-1.ui"
        ui_file = QFile(ui_file_name)
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
            sys.exit(-1)
        loader = QUiLoader()
        self.app = QApplication([])
        self.ui = loader.load(ui_file)
        ui_file.close()
        if not self.ui:
            print(loader.errorString())
            sys.exit(-1)

        # 按鍵動作測試
        self.ui.save_data_button.clicked.connect(self.say_hello)

    def say_hello(self):
        font = QFont()
        font.setPointSize(14)
        self.ui.input_display.setPlainText('Hello world!\nRun correctly')


if __name__ == "__main__":
    hb_window = HBMainWindow()
    hb_window.ui.show()
    hb_window.app.exec()
