from question_model import Question
from quiz_data import q_a
from quiz_brain import QuizBrain
from quiz_ui import QuizInterface
import html

question_bank = []
for i in range(len(q_a.get('Q'))):
    choices = []
    question_text = html.unescape(q_a['Q'][i])
    correct_answer = html.unescape(q_a["C_A"][i])
    incorrect_answers = q_a["I_A"][i]
    for ans in incorrect_answers:
        choices.append(html.unescape(ans))
    choices.append(correct_answer)
    new_question = Question(question_text, correct_answer, choices)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)

