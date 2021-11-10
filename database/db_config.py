import sqlite3
import os
from dotenv import load_dotenv

class DbConfig:

  def __init__(self):
    load_dotenv()
    super().__init__()

  def get_db(self):
    db = sqlite3.connect('unsri_guidebook.db')

    return db