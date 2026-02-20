from app.database import engine, Base


def create_db():
    Base.metadata.create_all(engine)