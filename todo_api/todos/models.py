class Category:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name


class Tag:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name


class ToDoTag:
    def __init__(self, todo_id, tag_id, id=None):
        self.id = id
        self.todo_id = todo_id
        self.tag_id = tag_id


class ToDo:
    def __init__(self, text, category, tags, id=None):
        self.id = id
        self.text = text
        self.category = category
        self.tags = tags

    def add_tag(self, tag):
        self.tags.append(tag)
