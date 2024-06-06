class Ad:
    def __init__(self, id, title, description, user_id, category_id, date_id):
        self.id = id
        self.title = title
        self.description = description
        self.user_id = user_id
        self.category_id = category_id
        self.date_id = date_id

    def __eq__(self, other):
        if not isinstance(other, Ad):
            return False
        return (self.id == other.id and self.title == other.title and
                self.description == other.description and self.user_id == other.user_id and
                self.category_id == other.category_id and self.date_id == other.date_id)

    def __repr__(self):
        return (f"Ad(id={self.id}, title={self.title}, description={self.description}, "
                f"user_id={self.user_id}, category_id={self.category_id}, date_id={self.date_id})")
