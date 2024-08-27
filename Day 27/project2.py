import random
import time
import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("600x400")
        self.questions = []
        self.score = 0
        self.hints_used = 0
        self.incorrect_answers = []
        self.current_question_index = 0
        self.current_category = None
        self.start_time = None
        self.difficulty = None
        self.load_sample_questions()
        self.create_main_menu()

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

    def create_main_menu(self):
        self.clear_window()

        label = tk.Label(self.root, text="Welcome to the Quiz Application", font=("Arial", 20))
        label.pack(pady=20)

        start_button = tk.Button(self.root, text="Start Quiz", command=self.start_quiz, font=("Arial", 14))
        start_button.pack(pady=10)

        exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, font=("Arial", 14))
        exit_button.pack(pady=10)

    def start_quiz(self):
        self.clear_window()
        self.select_category()

    def select_category(self):
        label = tk.Label(self.root, text="Select a Category", font=("Arial", 16))
        label.pack(pady=20)

        categories = list(self.questions.keys())
        for i, category in enumerate(categories):
            button = tk.Button(self.root, text=category, font=("Arial", 14),
                               command=lambda c=category: self.select_difficulty(c))
            button.pack(pady=5)

    def select_difficulty(self, category):
        self.current_category = category
        self.clear_window()

        label = tk.Label(self.root, text="Select Difficulty Level", font=("Arial", 16))
        label.pack(pady=20)

        difficulties = ['Easy', 'Medium', 'Hard']
        for i, level in enumerate(difficulties):
            button = tk.Button(self.root, text=level, font=("Arial", 14),
                               command=lambda d=level: self.begin_quiz(d))
            button.pack(pady=5)

    def begin_quiz(self, difficulty):
        self.difficulty = difficulty
        self.score = 0
        self.hints_used = 0
        self.incorrect_answers = []
        self.current_question_index = 0
        self.shuffle_questions(self.current_category)
        self.show_question()

    def shuffle_questions(self, category):
        random.shuffle(self.questions[category])

    def show_question(self):
        if self.current_question_index < len(self.questions[self.current_category]):
            self.clear_window()
            question_data = self.questions[self.current_category][self.current_question_index]

            label = tk.Label(self.root, text=f"Q{self.current_question_index + 1}: {question_data['question']}", font=("Arial", 16))
            label.pack(pady=20)

            for i, option in enumerate(question_data['options']):
                button = tk.Button(self.root, text=option, font=("Arial", 14),
                                   command=lambda ans=i: self.check_answer(ans, question_data['answer']))
                button.pack(pady=5)

            hint_button = tk.Button(self.root, text="Hint", font=("Arial", 14),
                                    command=lambda: self.provide_hint(question_data))
            hint_button.pack(pady=5)

            self.start_time = time.time()
        else:
            self.show_result()

    def provide_hint(self, question):
        self.hints_used += 1
        messagebox.showinfo("Hint", question['hint'])

    def check_answer(self, user_answer, correct_answer):
        elapsed_time = time.time() - self.start_time
        if elapsed_time > 10:
            messagebox.showinfo("Time's up!", "Time's up! Moving to the next question.")
            self.incorrect_answers.append(self.questions[self.current_category][self.current_question_index])
        elif user_answer == correct_answer:
            messagebox.showinfo("Correct", "Correct Answer!")
            self.score += 1
        else:
            messagebox.showinfo("Wrong", f"Wrong Answer! The correct answer was option {correct_answer + 1}.")
            self.incorrect_answers.append(self.questions[self.current_category][self.current_question_index])

        self.current_question_index += 1
        self.show_question()

    def show_result(self):
        self.clear_window()

        label = tk.Label(self.root, text="Quiz Completed!", font=("Arial", 20))
        label.pack(pady=20)

        total_questions = len(self.questions[self.current_category])
        percentage = (self.score / total_questions) * 100

        result_label = tk.Label(self.root, text=f"Your final score is: {self.score}/{total_questions}\nThat's {percentage:.2f}% correct.", font=("Arial", 16))
        result_label.pack(pady=10)

        self.award_badge(percentage)

        review_button = tk.Button(self.root, text="Review Incorrect Answers", command=self.review_incorrect_answers, font=("Arial", 14))
        review_button.pack(pady=5)

        exit_button = tk.Button(self.root, text="Exit", command=self.create_main_menu, font=("Arial", 14))
        exit_button.pack(pady=5)

    def award_badge(self, percentage):
        if percentage == 100:
            badge = "🌟 Excellent! You earned the Perfect Score Badge! 🌟"
        elif percentage >= 80:
            badge = "🎉 Great job! You earned the High Achiever Badge! 🎉"
        elif percentage >= 50:
            badge = "👍 Good effort! You earned the Pass Badge! 👍"
        else:
            badge = "Keep practicing! You'll improve with more practice."

        messagebox.showinfo("Badge Awarded", badge)

    def review_incorrect_answers(self):
        if self.incorrect_answers:
            review_window = tk.Toplevel(self.root)
            review_window.title("Review Incorrect Answers")
            review_window.geometry("600x400")

            label = tk.Label(review_window, text="Review your incorrect answers:", font=("Arial", 16))
            label.pack(pady=20)

            for question in self.incorrect_answers:
                question_label = tk.Label(review_window, text=f"Q: {question['question']}", font=("Arial", 14))
                question_label.pack(pady=5)

                answer_label = tk.Label(review_window, text=f"Correct Answer: {question['options'][question['answer']]}", font=("Arial", 14))
                answer_label.pack(pady=5)

            close_button = tk.Button(review_window, text="Close", command=review_window.destroy, font=("Arial", 14))
            close_button.pack(pady=10)
        else:
            messagebox.showinfo("No Incorrect Answers", "You have no incorrect answers to review.")

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()