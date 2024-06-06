from repositories.relational_repository import RelationalRepository
from models.User import User
from models.Ad import Ad
from models.Date import Date
from models.Category import Category
from models.Question import Question

class AdService:
    def __init__(self):
        self.repo = RelationalRepository()

    def add_user(self, user: User):
        self.repo.add_user(user)

    def get_user(self, user_id: int) -> User:
        return self.repo.get_user(user_id)

    def add_ad(self, ad: Ad):
        self.repo.add_ad(ad)

    def get_ad(self, ad_id: int) -> Ad:
        return self.repo.get_ad(ad_id)

    def add_date(self, date: Date):
        self.repo.add_date(date)

    def get_date(self, date_id: int) -> Date:
        return self.repo.get_date(date_id)

    def add_category(self, category: Category):
        self.repo.add_category(category)

    def get_category(self, category_id: int) -> Category:
        return self.repo.get_category(category_id)

    def add_question(self, question: Question):
        self.repo.add_question(question)

    def get_question(self, question_id: int) -> Question:
        return self.repo.get_question(question_id)
