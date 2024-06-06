from datetime import datetime
from models.User import User
from models.Ad import Ad
from models.Date import Date
from models.Category import Category
from models.Question import Question
from repositories.user_repository import UserRepository
from repositories.ad_repository import AdRepository
from repositories.date_repository import DateRepository
from repositories.category_repository import CategoryRepository
from repositories.question_repository import QuestionRepository

def main():
    # Initialize repositories
    user_repo = UserRepository()
    ad_repo = AdRepository()
    date_repo = DateRepository()
    category_repo = CategoryRepository()
    question_repo = QuestionRepository()

    # Example usage
    user1 = User(id=1, username="user1", email="user1@example.com")
    user2 = User(id=2, username="user2", email="user2@example.com")

    user_repo.add_user(user1)
    user_repo.add_user(user2)

    category = Category(id=1, name="Electronics")
    category_repo.add_category(category)

    date = Date(id=1, created_at=datetime.now())
    date_repo.add_date(date)

    ad = Ad(id=1, title="Selling a smartphone", description="Brand new smartphone", user_id=1, category_id=1, date_id=1)
    ad_repo.add_ad(ad)

    question = Question(id=1, ad_id=1, user_id=2, content="Is it still available?")
    question_repo.add_question(question)

    print(user_repo.get_user(1))
    print(ad_repo.get_ad(1))
    print(category_repo.get_category(1))
    print(date_repo.get_date(1))
    print(question_repo.get_question(1))

if __name__ == "__main__":
    main()
