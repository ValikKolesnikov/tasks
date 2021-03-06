CREATE TABLE News(
	Id SERIAL PRIMARY KEY,
	Title CHARACTER VARYING(50) NOT NULL,
	Text TEXT NOT NULL,
	Is_Published BOOLEAN NOT NULL,
	Category_id INTEGER NULL,
	Published_Date TIMESTAMP NOT NULL,
	FOREIGN KEY (Category_id) REFERENCES Category (id) ON DELETE SET NULL
);
CREATE TABLE Category(
	Id SERIAL PRIMARY KEY,
	Name CHARACTER VARYING(50) NOT NULL
);

-- 1.	Добавить запись в таблицу News

INSERT INTO News (Title, Text, Is_Published, Category_id)
VALUES ('Title', 'Text', true, NULL)

-- 2.	Добавить запись в таблицу Categories

INSERT INTO Category (Name)
VALUES ('Games')

-- 3.	Добавить 4 записи в таблицу Categories

INSERT INTO Category (Name)
VALUES ('Movies')
INSERT INTO Category (Name)
VALUES (‘Sport’)
INSERT INTO Category (Name)
VALUES ('Photo')
INSERT INTO Category (Name)
VALUES ('History')

-- 4.	Добавить 500 записей в таблицу News (название, текст не важен)


FOR i IN 1..500 LOOP
    INSERT INTO News (title, text, Is_Published, category_id, Published_Date) VALUES ('Title', 'Text', True, 4, '01.03.2000');
END LOOP;


-- 5.	Обновить название одной из записей в таблице Categories

UPDATE Category
SET name = 'Updated name'
WHERE id = 2

-- 6.	Обновить значение Is_Published в первых 10 записях таблицы News

UPDATE News
SET Is_Published = true
WHERE id in (SELECT id FROM News Limit 10)

-- 7.	Удалить запись из таблицы News

DELETE FROM News
WHERE id = 5

-- 8.	Удалить 100 последних записей из таблицы news

DELETE FROM News
WHERE id in (SELECT id FROM News ORDER BY id DESC LIMIT 100)

-- 9.	Удалить 1 запись из таблицы Categories

DELETE FROM Category
WHERE id = 1

-- 10.	Выбрать все записи из таблицы News, у которых Is_Published верно

SELECT id, title, text, Is_Published, category_id
FROM News
WHERE Is_Published = true

-- 11.	Выбрать все записи из таблицы News с включением имени соответствующей категории

SELECT n.id, n.title, n.text, n.Is_Published, c.name
FROM News n INNER JOIN Category c ON n.category_id = c.id

-- 12.	Выбрать все записи из таблицы News с включением соответствующей категории, у который Is_Published верно

SELECT n.id, n.title, n.text, n.Is_Published, c.name
FROM News n INNER JOIN Category c ON n.category_id = c.id
WHERE Is_Published = true

-- 13.	Выбрать все записи из таблицы Categories, у которых нет соответствия в таблице News

SELECT c.name
FROM Categories c INNER JOIN News n ON c.id = n.category_id
WHERE n.category_id IS NULL
-- 14.	Вывести количество записей в таблице News для каждой записи в таблице Categories. Отсортировать записи по имени категории в порядке возрастания и по Published_Date в порядке убывания


SELECT c.name, COUNT(*)
FROM News n INNER JOIN Category c ON n.category_id = c.id
GROUP BY c.id, n.category_id
ORDER BY c.name, n.Published_Date


-- 15.	Вывести количество записей в таблице News, у которых Is_Published верно, для каждой записи в таблице Categories


SELECT c.name, COUNT(*)
FROM Category c INNER JOIN News n ON c.id = n.category_id
WHERE n.Is_Published = true
GROUP BY c.id, n.category_id

-- 16.	Вывести количество записей в таблице News, у которых Is_Published верно и нет

SELECT Is_Published, COUNT(*)
FROM News
GROUP BY Is_Published

-- 17.	Вывести количество записей в таблице News, для каждой записи в таблице Categories, у  которых Is_Published верно и нет. Отсортировать записи по имени категории.

SELECT c.name, n.Is_Published, COUNT(*)
FROM Category c INNER JOIN News n ON c.id = n.category_id
GROUP BY c.id, n.category_id, n.Is_Published
ORDER BY c.name
