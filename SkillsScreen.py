from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import QBrush, QColor


lista1 = ['Habilidad1', 'Habilidad2']

options = {
    'Habilidad1': {
      'description': 'Prueba con el texto de la habilidad 1',
      'traits': ['1.2', '1.3', '1.4']
    },   
    'Habilidad2': {
      'description': 'Prueba con el texto de la habilidad 2',
      'traits': ['2.2', '2.3', '2.4']
    }
}


class SkillsScreen:

    def __init__(self) -> None:
        self.skillsScreen = uic.loadUi('gui/Configuration_1.ui')
        self.initGUI()
        self.skillsScreen.show()

    def initGUI(self,):
        self.setOptions()
        self.setListeners()

    def setOptions(self):
        self.skillsScreen.skill1_selection.addItems(['Selecciona una habilidad'] + lista1)
        self.skillsScreen.skill2_selection.addItems(['Selecciona una habilidad'] + lista1)

    def setListeners(self):        
        self.skillsScreen.skill1_selection.currentIndexChanged.connect(self.setSkill1Info)
        self.skillsScreen.skill2_selection.currentIndexChanged.connect(self.setSkill2Info)

    def setSkill1Info(self):
        skill = self.skillsScreen.skill1_selection.currentText()
        description, traits = '', ''

        if skill in lista1:
            description = options[skill]['description']
            traits = '\n'.join(options[skill]['traits'])

        self.skillsScreen.skill1_description.setText(description)
        self.skillsScreen.skill1_traits.setText(traits)
    
    def setSkill2Info(self):
        skill = self.skillsScreen.skill2_selection.currentText()
        description, traits = '', ''

        if skill in lista1:
            description = options[skill]['description']
            traits = '\n'.join(options[skill]['traits'])
            
        self.skillsScreen.skill2_description.setText(description)
        self.skillsScreen.skill2_traits.setText(traits)