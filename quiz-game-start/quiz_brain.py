class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.current_score=0
        self.question_list=q_list
    def check_answer(self,answer,current_question):
        if answer==(current_question.answer).lower():
            self.current_score+=1
            print("your answer is correct")
            print(f"Current score is {self.current_score}/{self.question_number}")
        else:
            print("wrong answer")    
            print(f"Correct answer is {current_question.answer}")
            print(f"Current score is {self.current_score}/{self.question_number}") 
    def still_has_a_question(self):
        if self.question_number==len(self.question_list):
            return False
        else:
            return True    

    def next_question(self):
        current_question=self.question_list[self.question_number]  
        self.question_number+=1
        answer=input(f"Q.{self.question_number}: {current_question.text} (True or False ?)").lower()
        self.check_answer(answer,current_question) 
        print("\n")
      
