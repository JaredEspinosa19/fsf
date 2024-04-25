from PyQt6.QtWidgets import QApplication
from SetUp import SetUp

class Feedback:
  def __init__(self) -> None:
    self.app = QApplication([])
    self.setUp = SetUp()
 
    self.app.exec()