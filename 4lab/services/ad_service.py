from repositories.xml_repository import XMLRepository
from models.User import User
from models.Ad import Ad
from models.Date import Date
from models.Category import Category
from models.Question import Question

class AdService:
    def __init__(self):
        self.xml_repo = XMLRepository()

    def add_ad(self, ad: Ad):
        self.xml_repo.add_ad(ad)

    def get_ad(self, ad_id: int) -> Ad:
        return self.xml_repo.get_ad(ad_id)

    def add_user(self, user: User):
        self.xml_repo.add_user(user)

    def get_user(self, user_id: int) -> User:
        return self.xml_repo.get_user(user_id)

    def add_date(self, date: Date):
        self.xml_repo.add_date(date)

    def get_date(self, date_id: int) -> Date:
        return self.xml_repo.get_date(date_id)

    def add_category(self, category: Category):
        self.xml_repo.add_category(category)

    def get_category(self, category_id: int) -> Category:
        return self.xml_repo.get_category(category_id)

    def add_question(self, question: Question):
        self.xml_repo.add_question(question)

    def get_question(self, question_id: int) -> Question:
        return self.xml_repo.get_question(question_id)

    # Example business rules
    def user_can_post_ad(self, user_id: int) -> bool:
        user = self.get_user(user_id)
        if not user:
            raise ValueError("User does not exist")
        if not user.email or "@" not in user.email:
            raise ValueError("User must have a valid email")
        return True

    def ad_can_have_questions(self, ad_id: int) -> bool:
        ad = self.get_ad(ad_id)
        if not ad:
            raise ValueError("Ad does not exist")
        return True

    def is_valid_category(self, category_id: int) -> bool:
        category = self.get_category(category_id)
        return category is not None
