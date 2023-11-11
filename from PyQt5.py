from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QTableWidget, QListWidget, QListWidgetItem,
QLineEdit, QFormLayout, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel, QSpinBox, QTextEdit)

app = QApplication([])
window = QWidget()
window.setWindowTitle("Таблиця")
window.resize(500,500)
window.move(400,400)
text = QTextEdit()
lab = QLabel()
lab.setText("речення")
lab1 = QLabel()
lab1.setText("речення")
lab2 = QLabel()
lab2.setText("речення")

one = QPushButton()
one.setText("кнопка")

two = QPushButton()
two.setText("кнопка")

three = QPushButton()
three.setText("кнопка")



four = QPushButton()
four.setText("кнопка")

tr = QHBoxLayout()
tl1 = QVBoxLayout()
tl2 = QVBoxLayout()
tl3 = QVBoxLayout()


tl1.addWidget(one)
tl1.addWidget(two)
tl1.addWidget(three)
tl1.addWidget(four)

tl2.addWidget(text)
tl3.addWidget(lab)
tl3.addWidget(lab1)
tl3.addWidget(lab2)

tr.addLayout(tl1)
tr.addLayout(tl2)
tr.addLayout(tl3)




window.setLayout(tr)
window.show()
app.exec_()