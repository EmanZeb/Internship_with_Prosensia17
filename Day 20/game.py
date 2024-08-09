def load_questions():
    questions = {
        "What is the capital of Pakistan?": "Islamabad",
        "Who made Pakistan?": "Muhammad Ali Jinnah",
        "What is the national game of Pakistan?": "Field Hockey",
        "Pakistan independence day?": "14 August 1947",
        "National animal of Pakistan?": "Markhor"
    }
    return questions
def ask_question(question, answer):  #Function to check whether input is correct or not
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        print("Correct!")
        return 1
    else:
        print(f"Sorry, that's incorrect. The correct answer is {answer}.")
        return 0
def main():    #show score
    questions = load_questions()
    score = 0
    for question, answer in questions.items():
        score += ask_question(question, answer)
    print(f"\nYour final score is {score} out of {len(questions)}.")
main()    #Run game