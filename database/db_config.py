import psycopg2
import asyncio

class DbConfig:
  def __init__(self):
    super().__init__()

  def get_db(self):
    db = psycopg2.connect(
        host = "127.0.0.1",
        port = "5432",
        database="unsri_guidebook",
        user="postgres",
        password="admin123"
      )

    return db
