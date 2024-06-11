from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class DesktopPet(QWidget):
    tool_name = '桌面宠物'
    def __init__(self, parent=None, **kwargs):
        super(DesktopPet, self).__init__(parent)
        self.index = 0
        self.show()
