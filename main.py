import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QRadioButton,
    QVBoxLayout,
    QWidget,
)

AlignCenter = Qt.AlignmentFlag.AlignCenter

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Конкурс від Crazy People")
window.resize(400, 200)

lb_question = QLabel('Як звали першого ютуб-блогера, який набрав 100000000 підписників?')

rb_ans1 = QRadioButton("Рет і Лінк")
rb_ans2 = QRadioButton("SlivkiShow")
rb_ans3 = QRadioButton("PewDiePie")
rb_ans4 = QRadioButton("TheBrianMaps")
rb_ans5 = QRadioButton("Mister Max")
rb_ans6 = QRadioButton("Mister Max")

vl_right_rb = QVBoxLayout()
vl_right_rb.addWidget(rb_ans1, alignment=AlignCenter)
vl_right_rb.addWidget(rb_ans2, alignment=AlignCenter)
vl_right_rb.addWidget(rb_ans3, alignment=AlignCenter)

vl_left_rb = QVBoxLayout()
vl_left_rb.addWidget(rb_ans4, alignment=AlignCenter)
vl_left_rb.addWidget(rb_ans5, alignment=AlignCenter)
vl_left_rb.addWidget(rb_ans6, alignment=AlignCenter)

hl_answers = QHBoxLayout()
hl_answers.addLayout(vl_right_rb)
hl_answers.addLayout(vl_left_rb)

vl_main = QVBoxLayout()
vl_main.addWidget(lb_question, alignment=AlignCenter)
vl_main.addLayout(hl_answers)

window.setLayout(vl_main)


def win():
    msg = QMessageBox()
    msg.setText("Ви виграли зустріч з творцями каналу!")
    msg.setWindowTitle("Повідомлення")
    msg.exec()


def lose():
    msg = QMessageBox()
    msg.setText("Ні, в 2005 році. Ви виграли фірмовий плакат")
    msg.setWindowTitle("Повідомлення")
    msg.exec()


rb_ans1.clicked.connect(lose)
rb_ans2.clicked.connect(lose)
rb_ans3.clicked.connect(win)
rb_ans4.clicked.connect(lose)
rb_ans5.clicked.connect(lose)
rb_ans6.clicked.connect(lose)

window.show()
app.exec()