#создай приложение для запоминания информации
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions = list()
questions.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions.append(Question('Какой национальности не существует?', 'Смурфы', 'Чумылцы', 'Энцы', 'Алеуты'))
questions.append(Question('На каком материке находится Россия?', 'Евразия', 'Австралия', 'Южная Америка', 'Северная Америка'))
questions.append(Question('Какой самый холодный материк?', 'Антарктида', 'Австралия', 'Евразия', 'Северная Америка'))
questions.append(Question('Какие самые высокие горы?', 'Гималаи', 'Кавзкие', 'Уральские горы', 'Альпы'))
questions.append(Question('Какой самый высокий вулкан в мире?', 'Охос-дель-Саладо', 'Килиманджаро', 'Сидли ', 'Демавенд '))
questions.append(Question('Сколько километров экватор Земли?', '40000 км', '90000 км', '25000 км ', '67000 км '))

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(500, 300)
lb_question = QLabel('Какой национальности не существует?')
button = QPushButton('Ответить')
radio_button_group = QGroupBox('Варианты ответов')
RadioGroup = QButtonGroup()
ans1 = QRadioButton('Энцы')
ans2 = QRadioButton('Чулымцы')
ans3 = QRadioButton('Смурфы')
ans4 = QRadioButton('Алеуты')
RadioGroup.addButton(ans1)
RadioGroup.addButton(ans2)
RadioGroup.addButton(ans3)
RadioGroup.addButton(ans4)
v_lay1 = QVBoxLayout()
v_lay2 = QVBoxLayout()
h_lay = QHBoxLayout()
v_lay1.addWidget(ans1)
v_lay1.addWidget(ans2)
v_lay2.addWidget(ans3)
v_lay2.addWidget(ans4)
h_lay.addLayout(v_lay1)
h_lay.addLayout(v_lay2)
radio_button_group.setLayout(h_lay)
radio_button_group.show()
AnsGroupBox = QGroupBox('Результат теста')
result = QLabel('Правильно/Неправильно')
correct_ans = QLabel('Правильный ответ')
ans_lay = QVBoxLayout()
ans_lay.addWidget(result)
ans_lay.addWidget(correct_ans, alignment = Qt.AlignCenter)
AnsGroupBox.setLayout(ans_lay)
AnsGroupBox.hide()
h_layout1 = QHBoxLayout()
h_layout2 = QHBoxLayout()
h_layout3 = QHBoxLayout()
h_layout1.addWidget(lb_question, alignment =(Qt.AlignHCenter | Qt.AlignVCenter))
h_layout2.addWidget(radio_button_group)
h_layout2.addWidget(AnsGroupBox)
h_layout3.addStretch(1)
h_layout3.addWidget(button, stretch = 2)
h_layout3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.addLayout(h_layout1, stretch = 2)
layout_card.addLayout(h_layout2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(h_layout3, stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
main_win.setLayout(layout_card)
def show_result():
    radio_button_group.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')
def show_question():
    radio_button_group.show()
    AnsGroupBox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [ans1, ans2, ans3, ans4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    correct_ans.setText(q.right_answer)
    show_question()
def check_answer():
    if answers[0].isChecked():
        result.setText('Правильно')
    if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        result.setText('Неправильно')
    show_result()

main_win.cur_question = -1

def next_question():
    main_win.cur_question += 1
    if main_win.cur_question == len(questions):
        main_win.cur_question = 0
    ask(questions[main_win.cur_question])

def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

next_question()
button.clicked.connect(click_OK)
main_win.show()
app.exec_()