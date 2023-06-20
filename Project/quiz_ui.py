from tkinter import Tk, Canvas, StringVar, Label, Radiobutton, Button, messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Тест по географии")
        self.window.geometry("850x530")

        # Отображение титула
        self.display_title()

        # Создаём холст для текста вопроса и отобразим вопрос на экран
        self.canvas = Canvas(width=800, height=250)
        self.question_text = self.canvas.create_text(400, 125,
                                                     text="Вопрос здесь",
                                                     width=680,
                                                     fill=THEME_COLOR,
                                                     font=(
                                                         'Ariel', 15, 'italic')
                                                     )
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.display_question()

        # Объявляем StringVar для хранения ответа пользователя
        self.user_answer = StringVar()

        # Отобразим четыре варианта (переключатели)
        self.opts = self.radio_buttons()
        self.display_options()

        # Чтобы показать, правильный это ответ или неправильный
        self.feedback = Label(self.window, pady=10, font=("ariel", 15, "bold"))
        self.feedback.place(x=300, y=380)

        # Следующий и кнопка выхода
        self.buttons()

        # Главный шлюз
        self.window.mainloop()

    def display_title(self):
        """Для отображения заголовка"""

        # титул
        title = Label(self.window, text="Тест на знания географии",
                      width=50, bg="green", fg="white", font=("ariel", 20, "bold"))

        # место расположения титула
        title.place(x=0, y=2)

    def display_question(self):
        """Чтобы отобразить вопрос"""

        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def radio_buttons(self):
        """Для создания четырех вариантов (переключателей)"""

        # инициализируем список пустым списком вариантов
        choice_list = []

        # позиция первого варианта
        y_pos = 220

        # добавление вариантов в список
        while len(choice_list) < 4:

            # настройка свойств переключателя
            radio_btn = Radiobutton(self.window, text="", variable=self.user_answer,
                                    value='', font=("ariel", 14))

            # добавление кнопки в список
            choice_list.append(radio_btn)

            # размещение кнопки
            radio_btn.place(x=200, y=y_pos)

            # увеличение положения оси y на 40
            y_pos += 40

        # возвращает переключатели
        return choice_list

    def display_options(self):
        """Для отображения четырех вариантов"""

        val = 0

        # Отмена выбора вариантов
        self.user_answer.set(None)

        # Пребирает варианты, которые будут отображаться для текста переключателей.
        for option in self.quiz.current_question.choices:
            self.opts[val]['text'] = option
            self.opts[val]['value'] = option
            val += 1

    def next_btn(self):
        """Чтобы показывать отзывы по каждому ответу и продолжать проверять наличие дополнительных вопросов"""

        # Проверяет, правильный ли ответ
        if self.quiz.check_answer(self.user_answer.get()):
            self.feedback["fg"] = "green"
            self.feedback["text"] = 'Правильный ответ! \U0001F44D'
        else:
            self.feedback['fg'] = 'red'
            self.feedback['text'] = ('\u274E Ой, неверно! \n'
                                     f'Правильный ответ: {self.quiz.current_question.correct_answer}')

        if self.quiz.has_more_questions():
            # Переходит к следующему, чтобы отобразить следующий вопрос и его варианты
            self.display_question()
            self.display_options()
        else:
            # Если вопросов больше нет, то отображается оценка
            self.display_result()

            # разрушает self.window
            self.window.destroy()

    def buttons(self):
        """Чтобы отобразить кнопку далее и кнопку выхода"""

        # Первая кнопка - это следующая кнопка для перехода к следующему вопросу
        next_button = Button(self.window, text="Проверка.\n Далее", command=self.next_btn,
                             width=18, bg="green", fg="white", font=("ariel", 16, "bold"))

        # нажатие кнопки на экране
        next_button.place(x=350, y=460)

        # Это вторая кнопка, которая используется для выхода из self.window
        quit_button = Button(self.window, text="Выйти", command=self.window.destroy,
                             width=5, bg="red", fg="white", font=("ariel", 16, " bold"))

        # Размещение кнопки выхода на экране
        quit_button.place(x=700, y=50)

    def display_result(self):
        """Чтобы отобразить результат с помощью окна сообщения"""
        correct, wrong, score_percent = self.quiz.get_score()

        correct = f"Правильно: {correct}"
        wrong = f"Ошибки: {wrong}"

        # Вычисляет процент правильных ответов
        result = f"Счёт: {score_percent}%"

        # Показывает окно сообщения для отображения результата
        messagebox.showinfo("Результат", f"{result}\n{correct}\n{wrong}")

