class Question:
    def __init__(self, id, ad_id, user_id, content):
        self.id = id
        self.ad_id = ad_id
        self.user_id = user_id
        self.content = content

    def __eq__(self, other):
        return (self.id == other.id and self.ad_id == other.ad_id and
                self.user_id == other.user_id and self.content == other.content)

    def __repr__(self):
        return f"Question(id={self.id}, ad_id={self.ad_id}, user_id={self.user_id}, content={self.content})"
