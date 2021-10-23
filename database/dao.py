import psycopg2
import asyncio
from database.db_config import DbConfig

class Dao:
  db = DbConfig().get_db()
  cursor = db.cursor()

  def __init__(self):
    super().__init__()

  def get_desc(self, name):
    try:
      self.cursor.execute("SELECT description FROM sarana_akademik WHERE name=" + "'" + name + "'")
      result = self.cursor.fetchone()

      return str(result[0])
    except Exception as e:
      print(e)
