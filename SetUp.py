from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QBrush, QColor
from Candidate import Candidate
from Files import Files
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

class SetUp:

    def __init__(self) -> None:
        self.setUp = uic.loadUi('gui/SetUp.ui')
        self.candidate = Candidate()
        self.files = Files()
        self.initGUI()
        self.setUp.show()

    def initGUI(self,):
        self.setUp.candidateInfoButton.clicked.connect(self.checkCandidateInfo)

    def checkCandidateInfo(self):
        
        if len(self.setUp.info1.text()) > 2 and re.fullmatch(regex, self.setUp.info2.text()) and len(self.setUp.info3.text()) > 3:
            self.candidate.setName(self.setUp.info1.text())
            self.candidate.setEmail(self.setUp.info2.text())
            self.candidate.setPosition(self.setUp.info3.text())

            self.setUp.b1.setBackgroundBrush(QColor("blue"))