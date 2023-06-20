class QuizBrain:

    def __init__(self, questions):
        self.question_no = 0
        self.score = 0
        self.questions = questions
        self.current_question = None

    def has_more_questions(self):
        """Чтобы проверить, есть ли в тесте еще вопросы"""

        return self.question_no < len(self.questions)

    def next_question(self):
        """Получить следующий вопрос, увеличив номер вопроса"""

        self.current_question = self.questions[self.question_no]
        self.question_no += 1
        q_text = self.current_question.question_text
        return f"Q.{self.question_no}: {q_text}"

    def check_answer(self, user_answer):
        """Сверить ответ пользователя с правильным ответом и поддерживать счёт"""

        correct_answer = self.current_question.correct_answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

    def get_score(self):
        """Получить количество правильных ответов, неправильных ответов и процент набранных баллов."""

        wrong = self.question_no - self.score
        score_percent = int(self.score / self.question_no * 100)
        return self.score, wrong, score_percent

