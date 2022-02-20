from question_bank import question_bank


class QuestionGame:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.correct = 0

    def ask_question(self):
        while self.question_number < len(self.question_list):
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            response = input(f"Q.{self.question_number}: {current_question.text}  (True/False): ").capitalize()
            if current_question.answer == response:
                self.correct += 1
                print(f'you answered correctly')
            else:
                print(f'you answered wrong ')
                print(f"the correct answer was {current_question.answer} ")

            print(f'you answerd {self.correct} / {self.question_number} question right')


q = QuestionGame(question_bank)

q.ask_question()

