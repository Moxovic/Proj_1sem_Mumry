import sqlite3 as sq

with sq.connect('dekanat.db') as con:
    cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""CREATE TABLE IF NOT EXISTS fakulteti (
 fakulteti_id INTEGER PRIMARY KEY AUTOINCREMENT,
 nazvanie_fakulteta VARCHAR
 )""")
# Создаем таблицу факультеты


with sq.connect('dekanat.db') as con:
    cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""CREATE TABLE IF NOT EXISTS kafedri (
 kafedri_id INTEGER PRIMARY KEY AUTOINCREMENT,
 nazvanie_kafedri VARCHAR,
 id_fakulteti INTEGER FOREIGN KEY
 )""")
# Создаем таблицу кафедры

with sq.connect('dekanat.db') as con:
    cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""CREATE TABLE IF NOT EXISTS specialnosti (
 specialnost_id INTEGER PRIMARY KEY AUTOINCREMENT,
 nazvanie_specialnosti VARCHAR,
 id_fakulteti INTEGER FOREIGN KEY
 )""")
# Создаём таблицу специальности
with sq.connect('dekanat.db') as con:
    cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""CREATE TABLE IF NOT EXISTS predmeti (
 predmeti_id INTEGER PRIMARY KEY AUTOINCREMENT,
 nazvanie_predmeta VARCHAR
 )""")
# Создаём таблицу предметы

with sq.connect('dekanat.db') as con:
    cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""CREATE TABLE IF NOT EXISTS forma_sdachi_predmeta (
 forma_sdachi_predmeta_id INTEGER PRIMARY KEY AUTOINCREMENT,
 nazvanie_forma_sdachi_predmeta VARCHAR
 )""")
# Создаём таблицу форма сдачи предмета

with sq.connect('dekanat.db') as con:
    cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""CREATE TABLE IF NOT EXISTS ychebni_plan (
 ychebni_plan_id INTEGER PRIMARY KEY AUTOINCREMENT,
 id_specialnost INTEGER FOREIGN KEY, 
 id_predmeti INTEGER FOREIGN KEY
  
 
 )""")