from flask import Flask, request, jsonify
from services.ad_service import AdService
from models.User import User
from models.Ad import Ad
from models.Date import Date
from models.Category import Category
from models.Question import Question
from datetime import datetime

app = Flask(__name__)
ad_service = AdService()

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    user = User(id=data['id'], username=data['username'], email=data['email'])
    ad_service.add_user(user)
    return jsonify({'message': 'User added successfully'}), 201

@app.route('/ads', methods=['POST'])
def add_ad():
    data = request.json
    ad = Ad(id=data['id'], title=data['title'], description=data['description'], user_id=data['user_id'], category_id=data['category_id'], date_id=data['date_id'])
    ad_service.add_ad(ad)
    return jsonify({'message': 'Ad added successfully'}), 201

@app.route('/categories', methods=['POST'])
def add_category():
    data = request.json
    category = Category(id=data['id'], name=data['name'])
    ad_service.add_category(category)
    return jsonify({'message': 'Category added successfully'}), 201

@app.route('/dates', methods=['POST'])
def add_date():
    data = request.json
    date = Date(id=data['id'], created_at=datetime.now())
    ad_service.add_date(date)
    return jsonify({'message': 'Date added successfully'}), 201

@app.route('/questions', methods=['POST'])
def add_question():
    data = request.json
    question = Question(id=data['id'], ad_id=data['ad_id'], user_id=data['user_id'], content=data['content'])
    ad_service.add_question(question)
    return jsonify({'message': 'Question added successfully'}), 201

if __name__ == "__main__":
    app.run(debug=True)
