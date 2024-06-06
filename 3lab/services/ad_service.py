from repositories.ad_repository import AdRepository
from repositories.user_repository import UserRepository
from repositories.date_repository import DateRepository
from repositories.category_repository import CategoryRepository
from repositories.question_repository import QuestionRepository
from models.Ad import Ad
from models.User import User
from models.Date import Date
from models.Category import Category
from models.Question import Question

class AdService:
    def __init__(self):
        self.ad_repo = AdRepository()
        self.user_repo = UserRepository()
        self.date_repo = DateRepository()
        self.category_repo = CategoryRepository()
        self.question_repo = QuestionRepository()

    def add_ad(self, ad):
        self.ad_repo.add_ad(ad)

    def get_ad(self, ad_id):
        return self.ad_repo.get_ad(ad_id)

    def add_user(self, user):
        self.user_repo.add_user(user)

    def get_user(self, user_id):
        return self.user_repo.get_user(user_id)

    def add_date(self, date):
        self.date_repo.add_date(date)

    def get_date(self, date_id):
        return self.date_repo.get_date(date_id)

    def add_category(self, category):
        self.category_repo.add_category(category)

    def get_category(self, category_id):
        return self.category_repo.get_category(category_id)

    def add_question(self, question):
        self.question_repo.add_question(question)

    def get_question(self, question_id):
        return self.question_repo.get_question(question_id)

    # Example business rules
    def user_can_post_ad(self, user_id):
        user = self.get_user(user_id)
        if not user:
            raise ValueError("User does not exist")
        # Example rule: user must have a valid email
        if not user.email or "@" not in user.email:
            raise ValueError("User must have a valid email")
        return True

    def ad_can_have_questions(self, ad_id):
        ad = self.get_ad(ad_id)
        if not ad:
            raise ValueError("Ad does not exist")
        return True

    def is_valid_category(self, category_id):
        category = self.get_category(category_id)
        return category is not None
