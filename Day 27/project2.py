import random
import time

class Quiz:
    def _init_(self):
        self.questions = []
        self.score = 0
        self.hints_used = 0
        self.incorrect_answers = []
        self.load_sample_questions()

    def load_sample_questions(self):
        self.questions = {
            'AI': [
                {'question': 'Who is known as the father of AI?', 'options': ['Alan Turing', 'John McCarthy', 'Geoffrey Hinton', 'Elon Musk'], 'answer': 1, 'hint': 'He coined the term "Artificial Intelligence".'},
                {'question': 'What is the main objective of AI?', 'options': ['Data Processing', 'Automation', 'Mimicking Human Intelligence', 'Networking'], 'answer': 2, 'hint': 'It involves cognitive functions similar to humans.'},
            ],
            'Coding': [
                {'question': 'Which language is considered the backbone of web development?', 'options': ['Python', 'Java', 'JavaScript', 'C++'], 'answer': 2, 'hint': 'It is commonly used for front-end and back-end web development.'},
                {'question': 'Which of the following is a version control system?', 'options': ['Git', 'Docker', 'Linux', 'Flask'], 'answer': 0, 'hint': 'It helps manage code changes in collaborative development.'},
            ],
            'Python': [
                {'question': 'Which data structure is used to store key-value pairs in Python?', 'options': ['List', 'Tuple', 'Dictionary', 'Set'], 'answer': 2, 'hint': 'It uses curly braces {}.'},
                {'question': 'Which keyword is used to define a function in Python?', 'options': ['func', 'def', 'lambda', 'define'], 'answer': 1, 'hint': 'It is followed by the function name.'},
            ]
        }

    def shuffle_questions(self, category):
        random.shuffle(self.questions[category])

    def display_question(self, question, q_num):
        print(f"Q{q_num + 1}: {question['question']}")
        for i, option in enumerate(question['options']):
            print(f"{i + 1}. {option}")
        start_time = time.time()
        user_answer = input("Enter the number of your answer (or type 'hint' for a hint): ")
        elapsed_time = time.time() - start_time
        return user_answer, elapsed_time

    def check_answer(self, user_answer, correct_answer):
        if user_answer.isdigit():
            return int(user_answer) - 1 == correct_answer
        return False

    def provide_hint(self, question):
        self.hints_used += 1
        print(f"Hint: {question['hint']}\n")

    def start_quiz(self):
        print("\nWelcome to the Quiz!")
        category = self.select_category()
        difficulty = self.select_difficulty()
        self.shuffle_questions(category)
        total_questions = len(self.questions[category])

        for i, question in enumerate(self.questions[category]):
            print(f"Difficulty: {difficulty}")
            user_answer, elapsed_time = self.display_question(question, i)

            if user_answer.lower() == 'hint':
                self.provide_hint(question)
                user_answer, _ = self.display_question(question, i)

            if elapsed_time > 10:
                print("Time's up! Moving to the next question.\n")
                self.incorrect_answers.append(question)
            elif self.check_answer(user_answer, question['answer']):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was option {question['answer'] + 1}.\n")
                self.incorrect_answers.append(question)

            self.show_progress(i + 1, total_questions)

        self.show_result(total_questions)
        self.review_incorrect_answers()

    def select_category(self):
        print("Select a category:")
        categories = list(self.questions.keys())
        for i, category in enumerate(categories):
            print(f"{i + 1}. {category}")
        choice = int(input("Enter the number of your category: ")) - 1
        return categories[choice]

    def select_difficulty(self):
        print("Select difficulty level:")
        difficulties = ['Easy', 'Medium', 'Hard']
        for i, level in enumerate(difficulties):
            print(f"{i + 1}. {level}")
        choice = int(input("Enter the number of your difficulty level: ")) - 1
        return difficulties[choice]

    def show_progress(self, current_question, total_questions):
        print(f"Progress: {current_question}/{total_questions} questions answered.\n")

    def show_result(self, total_questions):
        print("Quiz Completed!")
        print(f"Your final score is: {self.score}/{total_questions}")
        percentage = (self.score / total_questions) * 100
        print(f"That's {percentage:.2f}% correct.")
        self.award_badge(percentage)

    def award_badge(self, percentage):
        if percentage == 100:
            print("Excellent! You earned the Perfect Score Badge!")
        elif percentage >= 80:
            print("Great job! You earned the High Achiever Badge!")
        elif percentage >= 50:
            print("Good effort! You earned the Pass Badge!")
        else:
            print("Better luck next time. Keep practicing!")

    def review_incorrect_answers(self):
        if self.incorrect_answers:
            print("\nReview your incorrect answers:")
            for question in self.incorrect_answers:
                print(f"Q: {question['question']}")
                print(f"Correct Answer: {question['options'][question['answer']]}")
                print()

def main():
    quiz = Quiz()

    while True:
        print("Welcome To The Quiz Application")
        print("1. Start Quiz")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            quiz.start_quiz()
        elif choice == '2':
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()