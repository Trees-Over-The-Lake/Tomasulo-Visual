# This Python file uses the following encoding: utf-8
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtCore import pyqtSignal as Signal

import utils.os_utils as OsUtils

from window import Ui_MainWindow

class MainWindow(QMainWindow):

    instructions_loaded = Signal(str)

    def __init__(self):
        super().__init__()
        self.setupUi()

        self.setWindowTitle('TomasuluPy')
        self.showMaximized()

    def setupUi(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.stepButton.setEnabled(False)

    #@pyQtSlot
    def load_instructions_from_system(self):

        file_path = QFileDialog.getOpenFileName(
                    self,
                    str("Open instructions"),
                    OsUtils.get_user_home(),
                    filter="Text files (*.txt)")[0]

        if not file_path:
            return 

        self.ui.stepButton.setEnabled(True)

        self.instructions_loaded.emit(file_path)

    #@pyQtSlot
    def tomasulo_finalized(self):
        self.ui.stepButton.setEnabled(False)



if __name__ == "__main__":

    qt_app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(qt_app.exec())
