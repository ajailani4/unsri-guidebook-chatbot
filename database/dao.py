import psycopg2
from database.db_config import DbConfig

class Dao:
  db = DbConfig.get_db()
  cursor = db.cursor()

  def __init__(self):
    super().__init__()

  def get_desc(self, name):
    try:
      self.cursor.execute("SELECT desc FROM sarana_akademik WHERE name=" + name)
      result = self.cursor.fetchone()

      return result
    except Exception as e:
      print(e)
