from question_model import Question
from question_data import question_data

question_bank = []
for item in question_data:
    question = item["text"]
    answer = item['answer']
    new_question = Question(question,answer)
    question_bank.append(new_question)
print(question_bank)