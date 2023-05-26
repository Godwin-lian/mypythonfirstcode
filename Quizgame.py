'''a quiz game using Python.
The program present multiple-choice questions to the user
and keep track of their score.
You can store the questions and answers in a
file or a database and randomly select questions for each session.
'''
class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def play_game(self):
        for question in self.questions:
            print(question["question"])
            user_answer = input("Your answer: ")
            if user_answer.lower() == question["answer"].lower():
                self.score += 1
                print("Correct!")
            else:
                print(f"Incorrect. The correct answer is: {question['answer']}")
            print()

        print(f"Quiz finished. Your score: {self.score}/{len(self.questions)}")


# Example usage:
questions = [
    {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "answer": "Leonardo da Vinci"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "answer": "Jupiter"
    }
]

quiz_game = QuizGame(questions)
quiz_game.play_game()
