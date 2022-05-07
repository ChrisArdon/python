from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []  # This will be a list of Question objects
for question in question_data:
    question_text = question["text"]  # variable that holds the text from each dictionary in question_data
    question_answer = question["answer"]  # variable that holds the answer from each dictionary in question_data
    # here we create our object for each question in question_data
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)  # we append the object to our list

quiz = QuizBrain(question_bank)  # we create our object passing our list of questions

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")