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
 id_fakulteti INTEGER,
 FOREIGN KEY (id_fakulteti) REFERENCES fakulteti(id_fakulteti) ON DELETE CASCADE ON UPDATE CASCADE
 )""")
# Создаем таблицу кафедры


with sq.connect('dekanat.db') as con:
    cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""CREATE TABLE IF NOT EXISTS specialnosti (
 id_specialnost INTEGER PRIMARY KEY AUTOINCREMENT,
 nazvanie_specialnosti VARCHAR,
 id_kafedri INTEGER,
 FOREIGN KEY (id_kafedri) REFERENCES kafedri(id_kafedri) ON DELETE CASCADE ON UPDATE CASCADE
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
 id_specialnost INTEGER , 
 id_predmeti INTEGER ,
 id_forma_sdachi_predmeta INTEGER ,
 kol_vo_leksionnih_chasov INTEGER,
 kol_vo_prakticheskih_chasov INTEGER,
 kol_vo_laboratornih_chasov INTEGER,
 kursovaya_rabota BOOLEAN,
 
 FOREIGN KEY (id_specialnost) REFERENCES specialnosti(id_specialnost) ON DELETE CASCADE ON UPDATE CASCADE,
 FOREIGN KEY (id_predmeti) REFERENCES predmeti(id_predmeti) ON DELETE CASCADE ON UPDATE CASCADE,
 FOREIGN KEY (id_forma_sdachi_predmeta) REFERENCES forma_sdachi_predmeta(id_forma_sdachi_predmeta) ON DELETE CASCADE ON UPDATE CASCADE
 )""")
#Создаем таблицу учебный план

with sq.connect('dekanat.db') as con:
    cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""CREATE TABLE IF NOT EXISTS abiturients (
 id_abiturients INTEGER PRIMARY KEY,
 second_name TEXT,
 name_abiturients TEXT,
 surname TEXT,
 sex TEXT,
 date_born DATETIME,
 adress TEXT,
 phone TEXT,
 email TEXT,
 date_postup DATETIME,
 id_specialnost TEXT,
 FOREIGN KEY (id_specialnost) REFERENCES specialnosti(id_specialnost) ON DELETE CASCADE ON UPDATE CASCADE
 
 )""")
#Добавили приставку id к столбцу специальность для связи таблиц в бд 
# Создаем таблицу абитуриенты


with sq.connect('dekanat.db') as con:
    cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS users")
cur.execute("PRAGMA foreign_keys = ON")
cur.execute("""CREATE TABLE IF NOT EXISTS ucheb_karta (
 id_karta INTEGER PRIMARY KEY,
 fio_student TEXT,
 groupa TEXT,
 specialnost TEXT,
 id_predmeti TEXT ,
 id_forma_sdachi_predmeta TEXT,
 mark INTEGER,
 FOREIGN KEY (id_predmeti) REFERENCES predmeti(id_predmeti) ON DELETE CASCADE ON UPDATE CASCADE,
 FOREIGN KEY (id_forma_sdachi_predmeta) REFERENCES forma_sdachi_predmeta(id_forma_sdachi_predmeta) ON DELETE CASCADE ON UPDATE CASCADE
 )""")

# Создаем таблицу учебная карточка
#Тоже самое сделали и здесь со столбцами предметы и форма сдачи предмета
#FOREIGN KEY () REFERENCES TABLICA() ON DELETE CASCADE ON UPDATE CASCADE