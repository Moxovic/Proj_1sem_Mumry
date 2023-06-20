import requests
from googletrans import Translator

response = requests.get(url="https://opentdb.com/api.php?amount=45&category=22&difficulty=medium&type=multiple")
question_data = (response.json()["results"])


def translate_QA(text_trans):
    q = []
    correct_a = []
    incorrect_a = []
    for j in text_trans:
        q.append(Translator().translate(text=j['question'], dest='ru', src='en').text)
        correct_a.append(Translator().translate(text=j['correct_answer'], dest='ru', src='en').text)
        incorrect_a.append([Translator().translate(text=i, dest='ru', src='en').text for i in j['incorrect_answers']])
    return {'Q': q, 'C_A': correct_a, 'I_A': incorrect_a}


q_a = translate_QA(question_data)


