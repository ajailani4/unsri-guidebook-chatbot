import psycopg2

class DbConfig:
  def __init__(self):
    super().__init__()

  def get_db(self):
    db = None

    try:
      db = psycopg2.connect(
        host="localhost",
        database="sarana_akademik",
        user="postgres",
        password="admin123"
      )

      return db
    except (Exception, psycopg2.DatabaseError) as error:
      print(error)
    finally:
      if db is not None:
        db.close()
