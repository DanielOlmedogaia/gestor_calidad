from PyQt6 import QtWidgets, uic
import sys

class VistaTurno(QtWidgets.QDialog):

    def __init__(self, parent=None):        
        super(VistaTurno, self).__init__(parent)
        uic.loadUi("gui/turno.ui", self)
        self.pushButton_generar_turno.clicked.connect(self.generar_turno)
    def generar_turno(self):
        print("Este es un nuevo turno")
