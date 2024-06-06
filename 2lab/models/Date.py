from datetime import datetime

class Date:
    def __init__(self, id, created_at):
        self.id = id
        self.created_at = created_at

    def __eq__(self, other):
        return self.id == other.id and self.created_at == other.created_at

    def __repr__(self):
        return f"Date(id={self.id}, created_at={self.created_at})"
