from todos.models import Tag
from todos.repositories.todo_tag_repository import ToDoTagRepository
from todos.repositories.tag_repository import TagRepository

todo_tag_repo = ToDoTagRepository()
tag_repo = TagRepository()


def get_by_todo(todo):
    data = todo_tag_repo.get_by_todo(pk=todo.id)
    tags = []
    if data:
        for todo_tag_data in data:
            tag_id = todo_tag_data[2]
            tag_data = tag_repo.get(pk=tag_id)

            tags.append(Tag(id=tag_id, name=tag_data[1]))
        return tags
    else:
        return []
