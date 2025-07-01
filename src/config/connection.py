from sqlmodel import SQLModel, create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DB_PASSWORD = os.getenv("DB_PASSWORD")
DATABASE_URL = f"mysql+pymysql://root:{DB_PASSWORD}@172.17.0.2:3306/deckly"
print(DB_PASSWORD)
engine = create_engine(DATABASE_URL)

SQLModel.metadata.create_all(engine)
