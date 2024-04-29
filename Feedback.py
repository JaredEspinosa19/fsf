from PyQt6.QtWidgets import QApplication
from SetUp import SetUp
from SkillsScreen import SkillsScreen

class Feedback:
  def __init__(self) -> None:
    self.app = QApplication([])
    # self.setUp = SetUp()
    self.skillsScreen = SkillsScreen()
 
    self.app.exec()