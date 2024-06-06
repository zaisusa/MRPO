import xml.etree.ElementTree as ET
from models.User import User
from models.Ad import Ad
from models.Date import Date
from models.Category import Category
from models.Question import Question
from datetime import datetime

class XMLRepository:
    def __init__(self):
        self.users_file = 'users.xml'
        self.ads_file = 'ads.xml'
        self.dates_file = 'dates.xml'
        self.categories_file = 'categories.xml'
        self.questions_file = 'questions.xml'

    def _write_to_file(self, root, file_path):
        tree = ET.ElementTree(root)
        tree.write(file_path, encoding='utf-8', xml_declaration=True)

    def add_user(self, user: User):
        tree = ET.parse(self.users_file)
        root = tree.getroot()
        user_elem = ET.SubElement(root, 'User')
        user_elem.set('id', str(user.id))
        user_elem.set('username', user.username)
        user_elem.set('email', user.email)
        self._write_to_file(root, self.users_file)

    def get_user(self, user_id: int) -> User:
        tree = ET.parse(self.users_file)
        root = tree.getroot()
        user_elem = root.find(f"./User[@id='{user_id}']")
        if user_elem is not None:
            return User(id=int(user_elem.get('id')), username=user_elem.get('username'), email=user_elem.get('email'))
        return None

    def add_ad(self, ad: Ad):
        tree = ET.parse(self.ads_file)
        root = tree.getroot()
        ad_elem = ET.SubElement(root, 'Ad')
        ad_elem.set('id', str(ad.id))
        ad_elem.set('title', ad.title)
        ad_elem.set('description', ad.description)
        ad_elem.set('user_id', str(ad.user_id))
        ad_elem.set('category_id', str(ad.category_id))
        ad_elem.set('date_id', str(ad.date_id))
        self._write_to_file(root, self.ads_file)

    def get_ad(self, ad_id: int) -> Ad:
        tree = ET.parse(self.ads_file)
        root = tree.getroot()
        ad_elem = root.find(f"./Ad[@id='{ad_id}']")
        if ad_elem is not None:
            return Ad(id=int(ad_elem.get('id')), title=ad_elem.get('title'), description=ad_elem.get('description'), user_id=int(ad_elem.get('user_id')), category_id=int(ad_elem.get('category_id')), date_id=int(ad_elem.get('date_id')))
        return None

    def add_date(self, date: Date):
        tree = ET.parse(self.dates_file)
        root = tree.getroot()
        date_elem = ET.SubElement(root, 'Date')
        date_elem.set('id', str(date.id))
        date_elem.set('created_at', date.created_at.isoformat())
        self._write_to_file(root, self.dates_file)

    def get_date(self, date_id: int) -> Date:
        tree = ET.parse(self.dates_file)
        root = tree.getroot()
        date_elem = root.find(f"./Date[@id='{date_id}']")
        if date_elem is not None:
            return Date(id=int(date_elem.get('id')), created_at=datetime.fromisoformat(date_elem.get('created_at')))
        return None

    def add_category(self, category: Category):
        tree = ET.parse(self.categories_file)
        root = tree.getroot()
        category_elem = ET.SubElement(root, 'Category')
        category_elem.set('id', str(category.id))
        category_elem.set('name', category.name)
        self._write_to_file(root, self.categories_file)

    def get_category(self, category_id: int) -> Category:
        tree = ET.parse(self.categories_file)
        root = tree.getroot()
        category_elem = root.find(f"./Category[@id='{category_id}']")
        if category_elem is not None:
            return Category(id=int(category_elem.get('id')), name=category_elem.get('name'))
        return None

    def add_question(self, question: Question):
        tree = ET.parse(self.questions_file)
        root = tree.getroot()
        question_elem = ET.SubElement(root, 'Question')
        question_elem.set('id', str(question.id))
        question_elem.set('ad_id', str(question.ad_id))
        question_elem.set('user_id', str(question.user_id))
        question_elem.set('content', question.content)
        self._write_to_file(root, self.questions_file)

    def get_question(self, question_id: int) -> Question:
        tree = ET.parse(self.questions_file)
        root = tree.getroot()
        question_elem = root.find(f"./Question[@id='{question_id}']")
        if question_elem is not None:
            return Question(id=int(question_elem.get('id')), ad_id=int(question_elem.get('ad_id')), user_id=int(question_elem.get('user_id')), content=question_elem.get('content'))
        return None
