from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,QHBoxLayout, QGroupBox,QButtonGroup, QRadioButton, QPushButton, QLabel, QVBoxLayout)
from random import shuffle, randint


class Question():
    ''' contains the question, one correct answer and three incorrect asnwers'''
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer= right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list =[]
questions_list.append(Question('The state language of Brazil', 'Portugese', 'English', 'Spanish', 'Brazilian'))
questions_list.append(Question('When did the videogame Sonic the Hedgehog release?', '1991', '1987', '1999', '1983'))
questions_list.append(Question('What was the widest tornado ever?', 'El Reno, 2013', 'Moore, 1999', 'Xenia, 1974', 'Mayfield, 2021'))

        

app = QApplication([])

btn_OK = QPushButton('Answer')

lb_Question = QLabel('The most difficult question in the world!')
RadioGroupBox = QGroupBox('Answer options')


rbtn_1 = QRadioButton('Option 1')
rbtn_2 = QRadioButton('Option 2')
rbtn_3 = QRadioButton('Option 3')
rbtn_4 = QRadioButton('Option 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox("Test result")
lb_Result = QLabel('Are you correct or not?')
lb_correct =QLabel('the answer will be here')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft|Qt.AlignTop))
layout_res.addWidget(lb_correct, alignment=Qt.AlignHCenter, stretch = 2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignVCenter))

layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch = 2)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Next question')

def show_question():
    '''show question panel'''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Asnwer')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Right!')
        window.score += 1
        print('Statistics\n-Total questions:', window.total,'\n-Right asnwers:', window.score)
        print('Rating: ', (window.score/window.total*100,'%'))
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Wrong Answer!')
            print('Rating: ', (window.score/window.total*100,'%'))

def next_question():
    window.total += 1
    print('Statistics\n-Total questions:', window.total,'\n-Right asnwers:', window.score)
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)

def click_OK():
    ''' This determines whether to show another question or check the answer to this question'''
    if btn_OK.text() == 'Answer':
        check_answer()
    else:
        next_question()


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
window.score = 0
window.total = 0
btn_OK.clicked.connect(click_OK)
next_question()
window.resize(400, 400)
window.show()
app.exec()



