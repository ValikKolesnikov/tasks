CREATE TABLE News(
	id SERIAL PRIMARY KEY,
	title CHARACTER VARYING(50) NOT NULL,
	text text NOT NULL,
	is_published BOOLEAN NOT NULL,
	category_id INTEGER NULL,
	published_date TIMESTAMP NOT NULL,
	FOREIGN KEY (category_id) REFERENCES Category (id) ON DELETE SET NULL
);
CREATE TABLE Category(
	id SERIAL PRIMARY KEY,
	name CHARACTER VARYING(50) NOT NULL
);

-- 1.	Добавить запись в таблицу News

INSERT INTO News (title, text, is_published, category_id, published_date)
VALUES ('title', 'text', true, NULL, '24.05.21')

-- 2.	Добавить запись в таблицу Categories

INSERT INTO Category (name)
VALUES ('Games')

-- 3.	Добавить 4 записи в таблицу Categories

INSERT INTO Category (name)
VALUES ('Movies')
INSERT INTO Category (name)
VALUES (‘Sport’)
INSERT INTO Category (name)
VALUES ('Photo')
INSERT INTO Category (name)
VALUES ('History')

-- 4.	Добавить 500 записей в таблицу News (название, текст не важен)

DO
$do$
BEGIN
FOR i IN 1..500 LOOP
 	IF i < 250 THEN
    	INSERT INTO News (title, text, is_published, category_id, published_date) VALUES ('title', 'text', True, floor(random() * (6-1+1) + 1)::int, '01.03.2000');
		ELSE 
    	INSERT INTO News (title, text, is_published, category_id, published_date) VALUES ('title', 'text', False, floor(random() * (6-1+1) + 1)::int, '01.03.2000');
	END IF;
END LOOP;
END
$do$


-- 5.	Обновить название одной из записей в таблице Categories

UPDATE Category
SET name = 'Updated name'
WHERE id = 2

-- 6.	Обновить значение is_published в первых 10 записях таблицы News

UPDATE News
SET is_published = true
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

-- 10.	Выбрать все записи из таблицы News, у которых is_published верно

SELECT id, title, text, is_published, category_id
FROM News
WHERE is_published = true

-- 11.	Выбрать все записи из таблицы News с включением имени соответствующей категории

SELECT n.id, n.title, n.text, n.is_published, c.name
FROM News n INNER JOIN Category c ON n.category_id = c.id

-- 12.	Выбрать все записи из таблицы News с включением соответствующей категории, у который is_published верно

SELECT n.id, n.title, n.text, n.is_published, c.name
FROM News n INNER JOIN Category c ON n.category_id = c.id
WHERE is_published = true

-- 13.	Выбрать все записи из таблицы Categories, у которых нет соответствия в таблице News

SELECT c.name
FROM Categories c INNER JOIN News n ON c.id = n.category_id
WHERE n.category_id IS NULL
-- 14.	Вывести количество записей в таблице News для каждой записи в таблице Categories. Отсортировать записи по имени категории в порядке возрастания и по published_date в порядке убывания


SELECT c.name, COUNT(*)
FROM News n INNER JOIN Category c ON n.category_id = c.id
GROUP BY c.id, n.category_id
ORDER BY c.name, n.published_date


-- 15.	Вывести количество записей в таблице News, у которых is_published верно, для каждой записи в таблице Categories


SELECT c.name, COUNT(*)
FROM Category c INNER JOIN News n ON c.id = n.category_id
WHERE n.is_published = true
GROUP BY c.id, n.category_id

-- 16.	Вывести количество записей в таблице News, у которых is_published верно и нет

SELECT is_published, COUNT(*)
FROM News
GROUP BY is_published

-- 17.	Вывести количество записей в таблице News, для каждой записи в таблице Categories, у  которых is_published верно и нет. Отсортировать записи по имени категории.

SELECT c.name, n.is_published, COUNT(*)
FROM Category c INNER JOIN News n ON c.id = n.category_id
GROUP BY c.id, n.category_id, n.is_published
ORDER BY c.name

-- Еще один пункт:
-- Вывести только те записи из таблицы Categories, у которых количество IsPublished новостей больше или равно 1.

SELECT c.name, COUNT(n.is_published), n.is_published
FROM Category c INNER JOIN News n ON n.category_id = c.id
GROUP BY n.is_published, c.name
HAVING COUNT(n.is_published) >= 1 AND n.is_published = True