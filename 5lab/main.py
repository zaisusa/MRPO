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
    ad_service.add_user(user1)

    category = Category(id=1, name="Electronics")
    ad_service.add_category(category)

    date = Date(id=1, created_at=datetime.now())
    ad_service.add_date(date)

    ad = Ad(id=1, title="Smartphone for sale", description="Brand new smartphone", user_id=user1.id, category_id=category.id, date_id=date.id)
    ad_service.add_ad(ad)

    question = Question(id=1, ad_id=ad.id, user_id=user1.id, content="Is it still available?")
    ad_service.add_question(question)

    retrieved_ad = ad_service.get_ad(ad.id)
    print(f"Retrieved Ad: {retrieved_ad.title}, {retrieved_ad.description}")

if __name__ == "__main__":
    main()
