from PyQt6 import QtWidgets, uic
import sys
import ventana_turno

"""
La vista contiene los metodos para mostrar las ventanas emergentes y todo lo referente a la interfaz grafica
El modelo contiene las funciones de la logica de la aplicacion en nuestro caso contendra lo referente a los calculos y la base de datos
El controlador gestiona los metodos del modelo y la vista, interactua con ambos

"""
class Vista(QtWidgets.QMainWindow):

    def __init__(self):
        
        super(Vista, self).__init__()
        uic.loadUi("gui/MainWindow.ui", self)
        self.pushButton_turno.clicked.connect(self.show_ventana_turno)
    def show_ventana_turno(self):
        dialog = ventana_turno.VistaTurno(self)
        dialog.exec()
        
class Model:
    def __init__(self):
        self.turno=0
    
# Creamos el controlador
class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        # Conectamos los eventos de la vista con los métodos del controlador
        self.view.pushButton_turno.clicked.connect(self.muestra_ventana_turno)

    # Método para manejar el evento de un botón
    # Método para manejar el evento de un botón
    def muestra_ventana_turno(self):
        pass
        #number = self.view.get_number()
        #result_cuadrado = self.model.square(number)
        #result_cube=self.model.cube(number)
        #self.view.set_results(result_cuadrado,result_cube




if __name__ == '__main__':
    app=  QtWidgets.QApplication(sys.argv)
    view= Vista()
    model=Model()
    controller=Controller(view, model)
    view.show()
    sys.exit(app.exec())




