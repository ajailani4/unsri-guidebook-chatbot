from database.db_config import DbConfig

class Dao:
  db = DbConfig().get_db()
  cursor = db.cursor()

  def __init__(self):
    super().__init__()

  def get_academic_facil_desc(self, name):
    try:
      self.cursor.execute("SELECT description FROM sarana_akademik WHERE name=" + "'" + name + "'")
      result = self.cursor.fetchone()

      return str(result[0])
    except Exception as e:
      print(e)

  def get_academic_facil_schedule(self, name):
    try:
      self.cursor.execute("SELECT schedule FROM sarana_akademik WHERE name=" + "'" + name + "'")
      result = self.cursor.fetchone()

      return str(result[0])
    except Exception as e:
      print(e)

  def get_predicate_requirements(self, predikat, program):
    try:
      self.cursor.execute("SELECT syarat FROM predikat_kelulusan WHERE predikat=" + "'" + predikat + "'" + "AND program=" + "'" + program + "'")
      result = self.cursor.fetchone()

      if result is None:
        return ""
      else:
        return str(result[0])
      
    except Exception as e:
      print(e)