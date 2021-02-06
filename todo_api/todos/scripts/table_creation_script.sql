CREATE TABLE IF NOT EXISTS todos_todo
(
    id          INTEGER PRIMARY KEY,
    text        TEXT    NOT NULL,
    category_id INTEGER NULL,
    FOREIGN KEY (category_id) REFERENCES todos_category(id)
);

CREATE TABLE IF NOT EXISTS todos_tag
(
    id   INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS todos_category
(
    id   INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS todos_todo_tag
(
    id      INTEGER PRIMARY KEY,
    todo_id INTEGER NOT NULL,
    tag_id  INTEGER NOT NULL,
    FOREIGN KEY (todo_id) REFERENCES todos_todo(id),
    FOREIGN KEY (tag_id) REFERENCES todos_tag(id)
);