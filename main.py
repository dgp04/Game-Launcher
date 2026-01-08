from main_window import *
from PySide6.QtWidgets import QApplication, QMainWindow

class main_window(MainWindow):
    def __init__(self):
        super(main_window, self).__init__()
        self.setupUi(self)

app = QApplication([])
ventana = main_window()
ventana.show()
app.exec()