from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    obj_question = Question(data["text"],data["answer"])
    # print(data["text"])
    question_bank.append(obj_question)
    
quiz = QuizBrain(question_bank)
quiz.next_question()
