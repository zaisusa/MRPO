from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class UnitOfWork:
    def __init__(self, database_url='sqlite:///ads_service.db'):
        self.engine = create_engine(database_url)
        self.Session = sessionmaker(bind=self.engine)
        self.session = None

    def __enter__(self):
        self.session = self.Session()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.session.commit()
        else:
            self.session.rollback()
        self.session.close()
