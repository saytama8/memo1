from memo_card_layout import (
    app, layout_card,
    lb_Question, lb_Correct, lb_Result,
    btn_OK, show_question, show_result)

from PyQt5.QtWidgets import QWidget, QApplication
from random import shuffle

card_width, card_height = 600, 500

win_card = QWidget()
win_card.resize(card_width, card_height)
win_card.move(300, 300)
win_card.setWindowTitle("Memory Card")


win_card.setLayout(layout_card)
#show_data()
show_question()
#btn_OK.clicked.connect(click_OK)

win_card.show()
app.exec_()
