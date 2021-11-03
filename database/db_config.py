import psycopg2
import asyncio
import os
from dotenv import load_dotenv

class DbConfig:

  def __init__(self):
    load_dotenv()
    super().__init__()

  def get_db(self):
    db = psycopg2.connect(
        host = os.environ.get("HOST"),
        port = os.environ.get("PORT"),
        database = os.environ.get("DATABASE"),
        user = os.environ.get("USER"),
        password = os.environ.get("PASSWORD")
      )

    return db