CREATE TABLE IF NOT EXISTS todos_todo
(
    id          INTEGER PRIMARY KEY,
    text        TEXT    NOT NULL,
    category_id INTEGER NULL
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
    tag_id  INTEGER NOT NULL
);