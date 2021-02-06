from todos.models import ToDo, Category, Tag, ToDoTag
from todos.repositories.todo_repository import ToDoRepository
from todos.repositories.todo_tag_repository import ToDoTagRepository
import todos.services.category as category_service
import todos.services.tag as tag_service
import todos.services.todo_tag as todo_tag_service

todo_repo = ToDoRepository()
todo_tag_repo = ToDoTagRepository()


def create(text, category, tags):
    todo = ToDo(text=text, category=category, tags=[])
    todo_id = todo_repo.insert(todo)
    inserted_todo = get(todo_id)
    set_tags(todo=inserted_todo, tags_list=tags)
    return inserted_todo


def update(todo, text, category, tags):
    todo.text = text
    todo.category = category
    todo_repo.update(todo)
    set_tags(todo=todo, tags_list=tags)
    updated_todo = get(todo.id)
    return updated_todo


def get_all():
    todos = []
    data = todo_repo.get_all()
    for todo_data in data:
        id, text, category_id = todo_data
        category = category_service.get(pk=category_id) if category_id else None
        todo = ToDo(id=id, text=text, category=category, tags=[])
        tags = todo_tag_service.get_by_todo(todo)
        todo.tags = tags
        todos.append(todo)
    return todos


def get(pk):
    todo_data = todo_repo.get(pk=pk)
    if todo_data:
        id, text, category_id = todo_data
        category = category_service.get(pk=category_id) if category_id else None
        todo = ToDo(id=id, text=text, category=category, tags=[])
        tags = todo_tag_service.get_by_todo(todo)
        todo.tags = tags or []
        return todo
    else:
        return None


def delete(pk):
    todo_repo.delete(pk=pk)


def set_tags(todo, tags_list):
    for tag in tags_list:
        if tag.id not in [tag.id for tag in todo.tags]:
            todo_tag_repo.insert(ToDoTag(todo_id=todo.id, tag_id=tag.id))
    for tag in todo.tags:
        if tag.id not in [tag.id for tag in tags_list]:
            todo_tag_repo.delete(todo=todo, tag=tag)
    todo.tags = tags_list


def get_data_from_validation(serializer, validated_data):
    category_data = serializer.initial_data['category']
    tags_data = serializer.initial_data['tags']
    tags_ids = list(set([tag['id'] for tag in tags_data]))
    tags = []
    if tags_data:
        tags = [tag_service.get(pk=id) for id in tags_ids]
    category_id = category_data['id'] if category_data else None
    text = validated_data.get('text')
    category = category_service.get(pk=category_id)
    return {'category': category,
            'text': text,
            'tags': tags}
