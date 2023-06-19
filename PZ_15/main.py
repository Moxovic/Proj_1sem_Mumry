import sqlite3
import sqlite3 as sq

from Proj_1sem_Mumry.PZ_15.data_db import info_forma_sdachi_predmeta, \
    info_abiturients, info_fakultet, info_kafedra, info_specialnost, info_predmet, \
    info_uch_plan, info_uch_karta

with sq.connect('dekanat.db') as con:
    cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS fakultet")
cur.execute("PRAGMA foreign_keys = ON")
cur.execute("""CREATE TABLE IF NOT EXISTS fakultet
             (id_fakultet INTEGER PRIMARY KEY AUTOINCREMENT,
             nazvanie_fakultet TEXT)""")
# Создаем таблицу факультеты


with sq.connect('dekanat.db') as con:
    cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS kafedra")
cur.execute("PRAGMA foreign_keys = ON")
cur.execute("""CREATE TABLE IF NOT EXISTS kafedra
             (id_kafedra INTEGER PRIMARY KEY AUTOINCREMENT,
             nazvanie_kafedra TEXT,
             id_fakultet INTEGER,
             FOREIGN KEY (id_fakultet) REFERENCES fakultet(id_fakultet) ON DELETE CASCADE ON UPDATE CASCADE)""")
# Создаем таблицу кафедры


with sq.connect('dekanat.db') as con:
    cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS specialnost")
cur.execute("PRAGMA foreign_keys = ON")
cur.execute("""CREATE TABLE IF NOT EXISTS specialnost
             (id_specialnost INTEGER PRIMARY KEY AUTOINCREMENT,
             nazvanie_specialnost TEXT,
             id_kafedra INTEGER,
             FOREIGN KEY (id_kafedra) REFERENCES kafedra(id_kafedra) ON DELETE CASCADE ON UPDATE CASCADE)""")
# Создаём таблицу специальности


with sq.connect('dekanat.db') as con:
    cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS predmet")
cur.execute("PRAGMA foreign_keys = ON")
cur.execute("""CREATE TABLE IF NOT EXISTS predmet
             (id_predmet INTEGER PRIMARY KEY AUTOINCREMENT,
             nazvanie_predmet TEXT)""")
# Создаём таблицу предметы


with sq.connect('dekanat.db') as con:
    cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS forma_sdachi_predmeta")
cur.execute("PRAGMA foreign_keys = ON")
cur.execute("""CREATE TABLE IF NOT EXISTS forma_sdachi_predmeta
             (id_forma_sdachi_predmeta INTEGER PRIMARY KEY AUTOINCREMENT,
             nazvanie_forma_sdachi_predmeta TEXT)""")
# Создаём таблицу форма сдачи предмета

with sq.connect('dekanat.db') as con:
    cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS uch_plan")
cur.execute("PRAGMA foreign_keys = ON")
cur.execute("""CREATE TABLE IF NOT EXISTS uch_plan
             (id_uch_plan INTEGER PRIMARY KEY AUTOINCREMENT,
             id_specialnost INTEGER,
             id_predmet INTEGER,
             id_forma_sdachi_predmeta INTEGER,
             kol_lekcion_hour INTEGER,
             kol_pract_hour INTEGER,
             kol_lab_hour INTEGER,
             kursovaia BOOLEAN,
             FOREIGN KEY (id_specialnost) REFERENCES specialnost(id_specialnost) ON DELETE CASCADE ON UPDATE CASCADE,
             FOREIGN KEY (id_predmet) REFERENCES predmet(id_predmet) ON DELETE CASCADE ON UPDATE CASCADE,
             FOREIGN KEY (id_forma_sdachi_predmeta) REFERENCES forma_sdachi_predmeta(id_forma_sdachi_predmeta) ON DELETE CASCADE ON UPDATE CASCADE)""")
# Создаем таблицу учебный план

with sq.connect('dekanat.db') as con:
    cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS abiturients")
cur.execute("PRAGMA foreign_keys = ON")
cur.execute("""CREATE TABLE IF NOT EXISTS abiturients
             (id_abiturients INTEGER PRIMARY KEY AUTOINCREMENT,
             second_name TEXT,
             name TEXT,
             surname TEXT,
             sex TEXT,
             date_born DATE,
             adres TEXT,
             phone TEXT,
             Email TEXT,
             date_enroll DATE,
             id_specialnost INTEGER,
             FOREIGN KEY (id_specialnost) REFERENCES specialnost(id_specialnost) ON DELETE CASCADE ON UPDATE CASCADE)""")
# Добавили приставку id к столбцу специальность для связи таблиц в бд, также пришлось поменять тип на целочисленный
# Создаем таблицу абитуриенты


with sq.connect('dekanat.db') as con:
    cur = con.cursor()
# cur.execute("DROP TABLE IF EXISTS uch_karta")
cur.execute("PRAGMA foreign_keys = ON")
cur.execute("""CREATE TABLE IF NOT EXISTS uch_karta (
            id_uch_karta INTEGER PRIMARY KEY,
            fio TEXT,
            group TEXT,
            id_specialnost INTEGER,
            id_predmet INTEGER,
            id_forma_sdachi_predmeta INTEGER,
            mark INTEGER,
            FOREIGN KEY (id_specialnost) REFERENCES specialnost(id_specialnost) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (id_forma_sdachi_predmeta) REFERENCES forma_sdachi_predmeta(id_forma_sdachi_predmeta) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (id_predmet) REFERENCES predmet(id_predmet) ON DELETE CASCADE ON UPDATE CASCADE)""")

# Создаем таблицу учебная карточка
# Тоже самое сделали и здесь со столбцами предметы и форма сдачи предмета

# начинаем вставки

with sq.connect('dekanat.db') as con:
    cur = con.cursor()
cur.executemany("INSERT INTO fakultet VALUES (?, ?)", info_fakultet)  # факультеты вставка

with sq.connect('dekanat.db') as con:
    cur = con.cursor()
cur.executemany("INSERT INTO kafedra VALUES (?, ?, ?)", info_kafedra)  # кафедры вставка

with sq.connect('dekanat.db') as con:
    cur = con.cursor()
cur.executemany("INSERT INTO specialnost VALUES (?, ?, ?)", info_specialnost)  # специальности вставка

with sq.connect('dekanat.db') as con:
    cur = con.cursor()
cur.executemany("INSERT INTO predmet VALUES (?, ?)", info_predmet)  # предметы вставка

with sq.connect('dekanat.db') as con:
    cur = con.cursor()
cur.executemany("INSERT INTO forma_sdachi_predmeta VALUES (?, ?)",
                info_forma_sdachi_predmeta)  # форма сдачи предмета вставка

with sq.connect('dekanat.db') as con:
    cur = con.cursor()
cur.executemany("INSERT INTO uch_plan VALUES (?, ?, ?, ?, ?, ?, ?, ?)", info_uch_plan)  # учебный план вставка

with sq.connect('dekanat.db') as con:
    cur = con.cursor()
cur.executemany("INSERT INTO abiturients VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                info_abiturients)  # абитуриенты втсавка

with sq.connect('dekanat.db') as con:
    cur = con.cursor()
cur.executemany("INSERT INTO uch_karta VALUES (?, ?, ?, ?, ?, ?, ?)", info_uch_karta)  # учебная карта вставка

# начинаем селекты

with sqlite3.connect('decanat.db') as sq:
    # 1й запрос
    sq.execute("""
    SELECT uch_karta.fio, uch_karta.group, specialnost.nazvanie_specialnost
    FROM uch_karta
    JOIN specialnost ON uch_karta.id_specialnost = specialnost.id_specialnost
    JOIN fakultet ON specialnost.id_fakultet = fakultet.id_fakultet
    WHERE fakultet.nazvanie_fakultet = "Инф-ые технологий"
    GROUP BY ucheb_karta.fio_student;
    """)  # выводим список студентов на факультете Информационные технологии,к которому мы обратились по id,
    # с указацием группы 1й зпарос повлек за собой изменения, пришлось менять поле специальности(текст) в учебной
    # карте на внешний ключ к таблице специальности

    # 2й запрос
    sq.execute("""
    SELECT specialnost.nazvanie_specialnost, COUNT(uch_karta.id_uch_karta) AS count_students
    FROM specialnost
    INNER JOIN kafedra ON specialnost.id_kafedra = kafedra.id_kafedra
    INNER JOIN fakultet ON kafedra.id_fakultet = fakultet.id_fakultet
    INNER JOIN uch_karta ON specialnost.id_specialnost = uch_karta.id_specialnost
    WHERE fakultet.nazvanie_fakultet = "Тестирование программных продуктов и QA"
    GROUP BY specialnost.nazvanie_specialnost;
    """)  # Выводим список всех специальностей факультета и коичество студентов, обучающихся по каждой из них

    # 3й запрос
    sq.execute("""
    SELECT k.nazvanie_kafedra, COUNT(*) AS students_count
    FROM fakultet f
    JOIN kafedra k ON f.id_fakultet = k.id_fakultet
    JOIN specialnost s ON k.id_kafedra = s.id_kafedra
    JOIN uch_karta u ON s.id_specialnost = u.id_specialnost
    WHERE f.nazvanie_fakultet = "Математические науки"
    GROUP BY k.nazvanie_kafedra
    """)  # здесь мы выводим список кафедр факультета "Математические науки" и выводим количество студентов

    # 4й запрос
    sq.execute("""
    SELECT predmet.nazvanie_predmet, specialnost.nazvanie_specialnost, 
           SUM(uch_plan.kol_lekcion_hour + uch_plan.kol_pract_hour + uch_plan.kol_lab_hour) as total_hours
    FROM uch_plan
    JOIN specialnost ON specialnost.id_specialnost = uch_plan.id_specialnost
    JOIN predmet ON predmet.id_predmet = uch_plan.id_predmet
    GROUP BY predmet.id_predmet, specialnost.id_specialnost
    ORDER BY specialnost.nazvanie_specialnost, predmet.nazvanie_predmet;
    """)  # В этом запросе мы выводим список всех предметов и количесвто часов,
    # выделенных на каждый предмет  в учебном плане каждой специальности

    # 5й запрос
    sq.execute("""
    SELECT DISTINCT abiturients.surname || ' ' || abiturients.name AS fio
    FROM uch_karta 
    JOIN abiturients ON uch_karta.id_specialnost = abiturients.id_specialnost
    WHERE uch_karta.mark < 4
    ORDER BY abiturients.surname
    """)  # здесь мы выводим список студентов имеющих неудовлетворительные оценки. также используем оператор DISTINCT,
    # который исключает повторения
    # Также решили выпендриться и сделать сортировку по фамилиям

    # запрос 6 невозможен по условию, тк ни в одной из таблиц не было сказано о курсе студентов
    # Но мы нашли выход и взяли абитуриентов, тк это равносильно
    sq.execute("""
    SELECT DISTINCT predmet.nazvanie_predmet FROM uch_plan
    JOIN abiturients ON uch_plan.id_specialnost = abiturients.id_specialnost
    JOIN predmet ON uch_plan.id_predmet = predmet.id_predmet;
    """)

    # 7й запрос
    sq.execute("""
    SELECT a.second_name, a.name, a.surname
    FROM abiturients a
    JOIN uch_plan p ON a.id_specialnost = p.id_specialnost
    WHERE p.kursovaia = True;
    """)  # Здесь мы выводим фио студентов которые (просто)сдают курсовую (тк за семестры не было сказано в ТЗ)

    # 8й запрос
    sq.execute("""
    SELECT * FROM abiturients
    WHERE id_specialnost = (
    SELECT id_specialnost FROM specialnost 
    WHERE nazvanie_specialnost = "Cloud Engineer")
    """)  # выводим список всех абитуриентов, зачисленных на специальность "Cloud Engineer"

    # 9й запрос
    sq.execute("""
    SELECT DISTINCT predmet.nazvanie_predmet
    FROM uch_plan
    JOIN specialnost ON uch_plan.id_specialnost = specialnost.id_specialnost
    JOIN predmet ON uch_plan.id_predmet = predmet.id_predmet
    JOIN uch_karta ON uch_karta.id_specialnost = specialnost.id_specialnost AND uch_karta.id_predmet = predmet.id_predmet
    WHERE uch_karta.group = "3DD-1";
    """)  # выводим список всех предметов, которые изучают студенты группы "3DD-1", тк группы 101 у нас нет

    # 10 запрос
    # 10. Выводим список студентов и их оценки за все предметы на специальности
    # 'Cyber Security Engineer'
    sq.execute("""
    SELECT a.second_name, a.name, a.surname, p.nazvanie_predmet, uk.mark FROM abiturients a 
    JOIN uch_karta uk ON a.id_abiturients = uk.id_uch_karta 
    JOIN uch_plan up ON uk.id_specialnost = up.id_specialnost AND uk.id_predmet = up.id_predmet 
    JOIN predmet p ON up.id_predmet = p.id_predmet 
    JOIN specialnost s ON up.id_specialnost = s.id_specialnost 
    WHERE s.nazvanie_specialnost = 'Cyber Security Engineer' 
    ORDER BY a.second_name, a.name, a.surname, p.nazvanie_predmet;
    """)

    # SQL-запросы на обновление
    # 1 запрос
    sq.execute("""
    UPDATE fakultet
    SET nazvanie_fakultet = 'Новый факультет'
    WHERE id_fakultet = 1;
    """)  # здесь мы меняем название факультета с id=1 на Новый факультет

    # 2 запрос
    sq.execute("""
    UPDATE kafedra SET nazvanie_kafedra = 'Новая кафедра' WHERE id_kafedra = 2
    """)  # здесь бновляем названия кафедр с id=2 на "Новая кафедра"

    # 3 запрос
    sq.execute("""
    UPDATE specialnost SET nazvanie_specialnost="Новая специльаность" WHERE id_specialnost="3";
    """)  # здесь обновляем название специальности у всех специальностей с id=3

    # 4 запрос
    sq.execute("""
    UPDATE predmet SET nazvanie_predmet="Новый предмет" WHERE id_predmet="4";
    """)  # обновляем название предмета с id=4

    # 5 запрос
    sq.execute("""
    UPDATE forma_sdachi_predmeta SET nazvanie_forma_sdachi_predmeta="Новая форма сдачи" WHERE id_forma_sdachi_predmeta="5";
    """)  # обновляем форму сдачи предмета на НОВАЯ ФОРМА СДАЧИ с id=5

    # 6 запрос
    sq.execute("""
    UPDATE uch_plan SET kol_lekcion_hour = 30 WHERE id_uch_plan="6";
    """)  # Обновляем количество лекционных часов на 30 для учебного плана с id=6

    # 7 запрос
    sq.execute("""
    "UPDATE uch_plan SET kol_lekcion_hour = 5 WHERE id_specialnost = 7 AND id_predmet = 8");
    """)  # меняем количесвто лекционных часов на 5 на специальности "C#-developer" на предмете "Разработка на
    # UnrealEngine5"

    # 8запрос
    sq.execute("""
    UPDATE uch_plan
    SET kol_lab_hour = 1, id_forma_sdachi_predmeta = 8
    WHERE id_specialnost = (SELECT id_specialnost FROM specialnost WHERE nazvanie_specialnost = 'Assembly Engineer')
    AND id_predmet = (SELECT id_predmet FROM predmet WHERE nazvanie_predmet = 'Ассемблер и устройство процессора')
    """)  # изменяем количество лекционных часов на 1 у специальности  'Assembly Engineer' на предмете 'Ассемблер и
    # устройство процессора'

    # 9 запроос
    sq.execute("""
UPDATE uch_plan SET kol_lekcion_hour = 4, kol_pract_hour = 2
WHERE id_specialnost IN (
    SELECT id_specialnost
    FROM specialnost
    WHERE id_kafedra IN (
        SELECT id_kafedra
        FROM kafedra
        WHERE nazvanie_kafedra = 'Прикладное программирование'))
    AND id_predmet IN (
    SELECT id_predmet
    FROM predmet
    WHERE nazvanie_predmet = 'Основы проектирования Legacy проектов');
    """)  # здесь  мы  меняем количество лекционных и практических часов на специальности 'Прикладное программирование'
    # на предмете   'Основы проектирования Legacy проектов'

    # 10 запрос
    sq.execute("""
    UPDATE uch_plan
    SET kol_lekcion_hour = kol_lekcion_hour + 11
    WHERE kol_lekcion_hour > 30;
    """)  # обновляем кол-во лекционных часов (+11)  для всех предметов ,
    # у которых колирчество лекционных часов >30

    # 11 запрос
    sq.execute("""
     UPDATE abiturients SET second_name = 'Васильцов', name = 'Васька' 
     WHERE id_abiturients = 1;
    """)  # здесь присваем новое имя абитуриенту с id=1

    # 12
    sq.execute("""
    UPDATE kafedra SET nazvanie_kafedra = 'Новое название кафедры'
    WHERE id_kafedra = 1;
    UPDATE specialnost SET nazvanie_kafedra = 'Новое название кафедры'
    WHERE id_kafedra = 1;
    """)  # Данный запрос обновит название кафедры  в таблице kafedra
    # и specialnost на 'Новое название кафедры' для всех записей,
    # у которых id_kafedra равно 1.

    # 13
    sq.execute("""
    UPDATE uch_karta SET mark=5 
    WHERE id_uch_karta IN (SELECT id_uch_karta FROM uch_karta
    WHERE id_specialnost=5 AND id_predmet=5 
    AND id_forma_sdachi_predmeta=7 AND id_abiturients=3)
    """)  # здесь мы обновили оценку ПЕтрова Петра Петровича на 5
    #  с учетом специальности, предмета и формы сдачи предмета,
    #  к котрым мы обращались через айдишники
    # Очень мудреный запрос

    # 14
    sq.execute("""
    UPDATE specialnost SET nazvanie_specialnost = 'Новое название специальности для запроса 14' 
    WHERE id_specialnost = 2
    """)  # здесь мы обновляем название специальности с id=2

    # 15
    sq.execute("""
    UPDATE uch_karta
    SET mark = 5
    WHERE fio LIKE '%Иван%' AND id_predmet = (
      SELECT id_predmet
      FROM predmet
      WHERE nazvanie_predmet = 'JS и React'
    """)  # обновляtv все оценки на предмете "JS и React" у студентов с именем, содержащим подстроку "Иван",
    # устанавливая значение 5

    # 16
    sq.execute("""
    UPDATE fakultet
    SET nazvanie_fakultet = 'Факультет информационных технологий'
    WHERE nazvanie_fakultet = 'Математические науки';
    """)  # здесь изменяем название факультета 'Математические науки' на 'Факультет информационных технологий'

    # 17
    sq.execute("""
    UPDATE uch_plan SET kol_lab_hour =30 
    WHERE id_specialnost = (SELECT id_specialnost FROM specialnost 
    WHERE nazvanie_specialnost = 'OS Engineer') AND id_predmet = (SELECT id_predmet 
    FROM predmet 
    WHERE nazvanie_predmet = 'Администрирование Linux')
    """)  # Этот код обновит количество лабораторных часов для предмета 'Администрирование Linux'
    # и специальности 'OS Engineer', изменив количество часов на  30.

    # SQL delete запросы
    # 1
    sq.execute("""
    DELETE FROM abiturients WHERE date_enroll < '2020-01-01';
    """)  # этот запрос должен оставить лишь 1го студента из наштх данных

    # 2
    sq.execute("""
    DELETE FROM uch_plan
    WHERE id_specialnost NOT IN (SELECT id_specialnost FROM specialnost);
       """)  # этот запрос удаляет все учебные планы не связанные с какой либо специальностью. Здесь таких нет

    # ВАЖНАЯ ПОМЕТКА - Delete'ы имеют оченб простую структуру, поэтому мы не будем их пояснять
    # 3
    sq.execute("""
        DELETE FROM kafedra
        WHERE id_fakultet IS NULL;
           """)

    # 4
    sq.execute("""
    DELETE FROM predmet
    WHERE id_predmet NOT IN (
    SELECT DISTINCT id_predmet FROM uch_plan)
            """)

    # 5
    sq.execute("""
    DELETE FROM abiturients WHERE id_abiturients NOT IN 
        (SELECT DISTINCT id_uch_karta FROM uch_karta WHERE mark IS NOT NULL)
            """)

    # 6
    sq.execute("""
    DELETE FROM uch_karta WHERE id_predmet = (SELECT id_predmet FROM predmet
    WHERE nazvanie_predmet = 'Проектирование и разработка механизмов и машин специального назначения')
    AND id_forma_sdachi_predmeta = (SELECT id_forma_sdachi_predmeta 
    FROM forma_sdachi_predmeta WHERE nazvanie_forma_sdachi_predmeta = 'Письменный экзамен');
    """)

    # 7
    sq.execute("""
    DELETE FROM uch_karta
    WHERE id_specialnost IN (
        SELECT id_specialnost
        FROM specialnost
        JOIN kafedra ON specialnost.id_kafedra = kafedra.id_kafedra
        JOIN fakultet ON kafedra.id_fakultet = fakultet.id_fakultet
        WHERE fakultet.nazvanie_fakultet = 'Инф-ые технологии')
    """)

    # 8 запрос невозможен, тк условие вопроса некоректно сформулированно
    #     sq.execute("""
    # -
    #             """)

    # 9
    sq.execute("""
    DELETE FROM abiturients
    WHERE id_specialnost NOT IN (SELECT id_specialnost 
    FROM specialnost WHERE nazvanie_specialnost = 'Data Engineer')
    """)

    # 10 запрос невозможен по условию
    # sq.execute("""
    #         """)

    # 11 тоже самое
    # sq.execute("""
    #
    #         """)

    # 12 тоже самое
    # sq.execute("""
    #         """)

    # 13
    sq.execute("""
    DELETE FROM uch_karta
    WHERE id_forma_sdachi_predmeta = (
        SELECT id_forma_sdachi_predmeta FROM forma_sdachi_predmeta
        WHERE nazvanie_forma_sdachi_predmeta = 'Курсовая работа')
            """)

    # 14 запрос невозможен по условию
    sq.execute("""
         DELETE FROM kafedra
         WHERE id_fakultet IS NULL;
            """)

    # 15
    sq.execute("""
    DELETE FROM uch_karta
    WHERE id_specialnost IN
        (SELECT id_specialnost
        FROM specialnost
        WHERE nazvanie_specialnost = 'Инф-ые технологии')
            """)

    # 16запрос невозможен по условию
    # sq.execute("""
    #
    #         """)

    # 17 запрос невозможен по условию
    # sq.execute("""
    #
    #         """)
