class DateRepository:
    def __init__(self):
        self.dates = []

    def add_date(self, date):
        self.dates.append(date)

    def get_date(self, date_id):
        return next((date for date in self.dates if date.id == date_id), None)
