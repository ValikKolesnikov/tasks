INSERT INTO todos_category (name)
VALUES('HomeWork');

INSERT INTO todos_category (name)
VALUES('Job');

INSERT INTO todos_tag (name)
VALUES('good');

INSERT INTO todos_tag (name)
VALUES('cool');

INSERT INTO todos_tag (name)
VALUES('nice');

INSERT INTO todos_todo (text, category_id)
VALUES('Wash dish', 1);

INSERT INTO todos_todo (text, category_id)
VALUES('Watch TV', null);

INSERT INTO todos_todo (text, category_id)
VALUES('Do project', 2);

INSERT INTO todos_todo_tag (todo_id, tag_id)
VALUES (1, 1);

INSERT INTO todos_todo_tag (todo_id, tag_id)
VALUES (1, 2);

INSERT INTO todos_todo_tag (todo_id, tag_id)
VALUES (2, 2);