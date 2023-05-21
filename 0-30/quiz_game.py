class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer.lower() == self.answer.lower()
# class Allcourses:
#     """Models each Menu Item."""
#     def __init__(self, name,max_stu):
#         self.name = name
#         self.max_stu=max_stu
       
       


# class Course:
#     def __init__(self) -> None:
#         self.students=[]
#         self.allCourse = [
#             Allcourses(name="CPIT-455",max_stu=2),
#             Allcourses(name="CPIT-490",max_stu=3),
#             Allcourses(name="CPIT-405",max_stu=5)
#         ]

# class QuizGame:
#     def __init__(self):
#         self.questions = []
#         self.score = 0

#     def add_question(self, text, answer):
#         new_question = Question(text, answer)
#         self.questions.append(new_question)

#     def display_question(self, question):
#         print(question.text)
#         user_answer = input("Your answer: ")
#         if question.check_answer(user_answer):
#             print("Correct!")
#             self.score += 1
#         else:
#             print("Incorrect. The correct answer is:", question.answer)
#         print()

#     def run_game(self):
#         if len(self.questions) == 0:
#             print("No questions available.")
#             return

#         print("Welcome to the Quiz Game!")
#         print("Answer the following questions:")
#         print()

#         self.score = 0

#         for question in self.questions:
#             self.display_question(question)

#         print("Quiz complete! You scored {} out of {}.".format(self.score, len(self.questions)))


# # Create an instance of the QuizGame
# quiz = QuizGame()

# # Add questions to the quiz
# quiz.add_question("What is the capital of France?", "Paris")
# quiz.add_question("What is the largest planet in our solar system?", "Jupiter")
# quiz.add_question("What year was Python first released?", "1991")

# # Run the quiz game
# quiz.run_game()


