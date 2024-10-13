# create_tables.py
from database import Base, engine
from models import ImageModel

Base.metadata.create_all(bind=engine)
