CREATE TABLE News(
	Id SERIAL PRIMARY KEY,
	Title CHARACTER VARYING(50) NOT NULL,
	Text TEXT NOT NULL,
	IsPublished BOOLEAN NOT NULL,
	Category_id INTEGER NULL,
	PublishedDate TIMESTAMP NOT NULL,
	FOREIGN KEY (Category_id) REFERENCES Category (id) ON DELETE SET NULL
);
CREATE TABLE Category(
	Id SERIAL PRIMARY KEY,
	Name CHARACTER VARYING(50) NOT NULL
);

-- 1.	Добавить запись в таблицу News

INSERT INTO News (Title, Text, IsPublished, Category_id)
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

INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 5, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 5, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 2, '01.03.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2000');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 3, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '01.02.2010');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', False, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 2, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 4, '05.07.2020');
INSERT INTO News (title, text, ispublished, category_id, PublishedDate)VALUES ('Title', 'Text', True, 3, '05.07.2020');


-- 5.	Обновить название одной из записей в таблице Categories

UPDATE Category
SET name = 'Updated name'
WHERE id = 2

-- 6.	Обновить значение IsPublished в первых 10 записях таблицы News

UPDATE News
SET ispublished = true
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

-- 10.	Выбрать все записи из таблицы News, у которых IsPublished верно

SELECT id, title, text, ispublished, category_id
FROM News
WHERE ispublished = true

-- 11.	Выбрать все записи из таблицы News с включением имени соответствующей категории

SELECT n.id, n.title, n.text, n.ispublished, c.name
FROM News n INNER JOIN Category c ON n.category_id = c.id

-- 12.	Выбрать все записи из таблицы News с включением соответствующей категории, у который IsPublished верно

SELECT n.id, n.title, n.text, n.ispublished, c.name
FROM News n INNER JOIN Category c ON n.category_id = c.id
WHERE ispublished = true

-- 13.	Выбрать все записи из таблицы Categories, у которых нет соответствия в таблице News

SELECT id, title, text, ispublished
FROM News
WHERE category_id IS NULL
-- 14.	Вывести количество записей в таблице News для каждой записи в таблице Categories. Отсортировать записи по имени категории в порядке возрастания и по PublishedDate в порядке убывания


SELECT c.name, COUNT(*)
FROM News n INNER JOIN Category c ON n.category_id = c.id
GROUP BY c.id, n.category_id
ORDER BY c.name, n.publisheddate


-- 15.	Вывести количество записей в таблице News, у которых IsPublished верно, для каждой записи в таблице Categories


SELECT c.name, COUNT(*)
FROM News n INNER JOIN Category c ON n.category_id = c.id
WHERE n.ispublished = true
GROUP BY c.id, n.category_id

-- 16.	Вывести количество записей в таблице News, у которых IsPublished верно и нет

SELECT ispublished, COUNT(*)
FROM News
GROUP BY ispublished

-- 17.	Вывести количество записей в таблице News, для каждой записи в таблице Categories, у  которых IsPublished верно и нет. Отсортировать записи по имени категории.

SELECT c.name, n.ispublished, COUNT(*)
FROM News n INNER JOIN Category c ON n.category_id = c.id
GROUP BY c.id, n.category_id, n.ispublished
ORDER BY c.name
