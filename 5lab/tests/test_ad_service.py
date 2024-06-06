import unittest
from datetime import datetime
from models.User import User
from models.Ad import Ad
from models.Date import Date
from models.Category import Category
from models.Question import Question
from services.ad_service import AdService

class TestAdService(unittest.TestCase):

    def setUp(self):
        self.service = AdService()
        self.user = User(id=1, username="user1", email="user1@example.com")
        self.service.add_user(self.user)
        self.category = Category(id=1, name="Electronics")
        self.service.add_category(self.category)
        self.date = Date(id=1, created_at=datetime.now())
        self.service.add_date(self.date)
        self.ad = Ad(id=1, title="Selling a smartphone", description="Brand new smartphone", user_id=1, category_id=1, date_id=1)
        self.service.add_ad(self.ad)
        self.question = Question(id=1, ad_id=1, user_id=1, content="Is it still available?")
        self.service.add_question(self.question)

    def test_user_can_post_ad(self):
        self.assertTrue(self.service.user_can_post_ad(self.user.id))

    def test_ad_can_have_questions(self):
        self.assertTrue(self.service.ad_can_have_questions(self.ad.id))

    def test_is_valid_category(self):
        self.assertTrue(self.service.is_valid_category(self.category.id))

    def test_get_user(self):
        self.assertEqual(self.service.get_user(self.user.id), self.user)

    def test_get_ad(self):
        self.assertEqual(self.service.get_ad(self.ad.id), self.ad)

    def test_get_category(self):
        self.assertEqual(self.service.get_category(self.category.id), self.category)

    def test_get_date(self):
        self.assertEqual(self.service.get_date(self.date.id), self.date)

    def test_get_question(self):
        self.assertEqual(self.service.get_question(self.question.id), self.question)

if __name__ == "__main__":
    unittest.main()
