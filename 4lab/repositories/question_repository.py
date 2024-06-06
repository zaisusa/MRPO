class QuestionRepository:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def get_question(self, question_id):
        return next((question for question in self.questions if question.id == question_id), None)
