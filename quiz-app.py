class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def is_correct(self, user_answer):
        return self.answer == user_answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run(self):
        for question in self.questions:
            print(question.question)
            for idx, option in enumerate(question.options, start=1):
                print(f"{idx}. {option}")
            user_answer = int(input("Enter your answer: "))
            if question.is_correct(user_answer):
                self.score += 1

        print(f"You scored {self.score} out of {len(self.questions)}!")


questions = [
    Question("What's the capital of France?", ["Paris", "Berlin", "London"], 1),
    Question("What's the capital of Germany?", ["Rome", "Berlin", "London"], 2),
    Question("What's the capital of England?", ["Edinburgh", "Paris", "London"], 3)
]

quiz = Quiz(questions)
quiz.run()