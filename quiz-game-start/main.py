from data import question_data
from quiz_brain import QuizBrain
from question_model import Question
question_bank = []
for i in question_data:
    question=i["text"]
    answer=i["answer"]
    new_question=Question(question,answer)
    question_bank.append(new_question)
quiz=QuizBrain(question_bank)
while quiz.still_has_a_question():  
    quiz.next_question()
print("you have completed a quiz")
print(f"you currents score is{quiz.current_score}/{len(question_bank)}")    


