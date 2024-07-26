from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for item in question_data:
    # print(item)
    quetsion_text=item["text"]
    quetsion_answer = item["answer"]
    new_question=Question(quetsion_text,quetsion_answer)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("The quiz is completed!")
print(f"Your final score is:{quiz.score}/{quiz.question_number}")

