from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

app=QApplication([])

win=QWidget()

win.resize(800,600)

win.setWindowTitle("Hello, World!")

win.show()
app.exec_()