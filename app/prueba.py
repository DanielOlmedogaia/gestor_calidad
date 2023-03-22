import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QDialog, QLineEdit, QLabel,QDialogButtonBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel


class Model:
    def __init__(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('data.db')
        self.db.open()
        
        query = QSqlQuery()
        query.exec_("create table if not exists users(id integer primary key, name varchar(20))")
        
        self.table_model = QSqlTableModel()
        self.table_model.setTable('users')
        self.table_model.select()

    def add_user(self, name):
        record = self.table_model.record()
        record.setValue('name', name)
        self.table_model.insertRecord(-1, record)
        self.table_model.select()

    def delete_user(self, row):
        self.table_model.removeRow(row)
        self.table_model.select()

class View(QMainWindow):
    def __init__(self):
        super().__init__()

        self.table_view = QTableView()

        add_button = QPushButton('Agregar usuario')
        add_button.clicked.connect(self.show_add_user_dialog)

        delete_button = QPushButton('Eliminar usuario')
        delete_button.clicked.connect(self.delete_user)

        button_layout = QHBoxLayout()
        button_layout.addWidget(add_button)
        button_layout.addWidget(delete_button)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.table_view)
        main_layout.addLayout(button_layout)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def show_add_user_dialog(self):
        dialog = AddUserDialog(self)
        dialog.exec_()

    def delete_user(self):
        selected = self.table_view.selectedIndexes()
        if selected:
            row = selected[0].row()
            controller.delete_user(row)

class AddUserDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.name_edit = QLineEdit()
        self.name_label = QLabel('Nombre:')

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_edit)
        layout.addWidget(button_box)

        self.setLayout(layout)

    def accept(self):
        name = self.name_edit.text()
        controller.add_user(name)
        super().accept()

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.table_view.setModel(self.model.table_model)

    def add_user(self, name):
        self.model.add_user(name)

    def delete_user(self, row):
        self.model.delete_user(row)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = Model()
    view = View()
    controller = Controller(model, view)
    view.show()
    sys.exit(app.exec_())
