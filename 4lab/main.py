from datetime import datetime
from models.User import User
from models.Ad import Ad
from models.Date import Date
from models.Category import Category
from models.Question import Question
from services.ad_service import AdService

def main():
    # Initialize service
    ad_service = AdService()

    # Example usage
    user1 = User(id=1, username="user1", email="user1@example.com")
    user2 = User(id=2, username="user2", email="user2@example.com")

    ad_service.add_user(user1)
    ad_service.add_user(user2)

    date1 = Date(id=1, created_at=datetime.now())
    ad_service.add_date(date1)

    category1 = Category(id=1, name="Electronics")
    ad_service.add_category(category1)

    ad1 = Ad(id=1, title="iPhone for sale", description="Selling my iPhone", user_id=1, category_id=1, date_id=1)
    ad_service.add_ad(ad1)

    question1 = Question(id=1, ad_id=1, user_id=2, content="Is it still available?")
    ad_service.add_question(question1)

    # Fetch and print to verify
    fetched_user = ad_service.get_user(1)
    fetched_ad = ad_service.get_ad(1)
    fetched_date = ad_service.get_date(1)
    fetched_category = ad_service.get_category(1)
    fetched_question = ad_service.get_question(1)

    print(fetched_user)
    print(fetched_ad)
    print(fetched_date)
    print(fetched_category)
    print(fetched_question)

if __name__ == "__main__":
    main()
