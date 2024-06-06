class CategoryRepository:
    def __init__(self):
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)

    def get_category(self, category_id):
        return next((category for category in self.categories if category.id == category_id), None)
