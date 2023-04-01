import sqlite3 as sq

with sq.connect('dekanat.db') as con:
    cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""CREATE TABLE IF NOT EXISTS fakulteti (
 id_fakulteti INTEGER PRIMARY KEY AUTOINCREMENT,
 nazvanie_fakulteta VARCHAR
 )""")
# Создаем таблицу факультеты


with sq.connect('dekanat.db') as con:
    cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""CREATE TABLE IF NOT EXISTS kafedri (
 id_kafedri INTEGER PRIMARY KEY AUTOINCREMENT,
 nazvanie_kafedri VARCHAR,
 id_fakulteti INTEGER FOREIGN KEY
 )""")
# Создаем таблицу кафедры

with sq.connect('dekanat.db') as con:
    cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""CREATE TABLE IF NOT EXISTS specialnosti (
 id_specialnost INTEGER PRIMARY KEY AUTOINCREMENT,
 nazvanie_specialnosti VARCHAR,
 id_fakulteti INTEGER FOREIGN KEY
 )""")
# Создаём таблицу специальности
with sq.connect('dekanat.db') as con:
    cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""CREATE TABLE IF NOT EXISTS predmeti (
 id_predmeti INTEGER PRIMARY KEY AUTOINCREMENT,
 nazvanie_predmeta VARCHAR
 )""")
# Создаём таблицу предметы

with sq.connect('dekanat.db') as con:
    cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""CREATE TABLE IF NOT EXISTS forma_sdachi_predmeta (
 id_forma_sdachi_predmeta INTEGER PRIMARY KEY AUTOINCREMENT,
 nazvanie_forma_sdachi_predmeta VARCHAR
 )""")
# Создаём таблицу форма сдачи предмета

with sq.connect('dekanat.db') as con:
    cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""CREATE TABLE IF NOT EXISTS ychebni_plan (
 id_ychebni_plan INTEGER PRIMARY KEY AUTOINCREMENT,
 id_specialnost INTEGER FOREIGN KEY, 
 id_predmeti INTEGER FOREIGN KEY,
 id_forma_sdachi_predmeta INTEGER FOREIGN KEY,
 kol_vo_leksionnih_chasov INTEGER,
 kol_vo_prakticheskih_chasov INTEGER,
 kol_vo_laboratornih_chasov INTEGER,
 kursovaya_rabota BOOLEAN
 )""")
#Создаем таблицу учебный план

with sq.connect('dekanat.db') as con:
    cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""CREATE TABLE IF NOT EXISTS abiturients (
 id_abiturients INTEGER PRIMARY KEY,
 second_name TEXT,
 name TEXT,
 surname TEXT,
 sex TEXT,
 date_born DATETIME,
 adress TEXT,
 phone TEXT,
 email TEXT,
 date_postup DATETIME,
 specialnost TEXT
 )""")

#Создаем таблицу абитуриенты

with sq.connect('dekanat.db') as con:
    cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS users")
cur.execute("PRAGMA foreign_keys = ON")
cur.execute("""CREATE TABLE IF NOT EXISTS ucheb_karta (
 id_karta INTEGER PRIMARY KEY,
 fio_student TEXT,
 group TEXT,
 specialnost TEXT,
 predmet TEXT FOREIGN KEY,
 forma_sdachi_predmeta TEXT FOREIGN KEY,
 mark INTEGER
 FOREIGN KEY () REFERENCES TABLICA() ON DELETE CASCADE ON UPDATE CASCADE
 )""")

#Создаем таблицу учебная карточка