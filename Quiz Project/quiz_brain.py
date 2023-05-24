class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        display_question = self.question_list[self.question_number].text
        correct_answer = self.question_list[self.question_number].answer
        ans = input(f"Q.{self.question_number + 1}: {display_question}. (True/False): ")
        self.question_number += 1
        self.check_answer(ans, correct_answer)

    def check_answer(self, ans, correct_answer):
        if ans.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
