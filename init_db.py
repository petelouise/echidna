from database import db
from models import Image, ImageFeature


def initialize_database():
    db.connect()
    db.create_tables([Image, ImageFeature])
    db.close()


if __name__ == "__main__":
    initialize_database()
