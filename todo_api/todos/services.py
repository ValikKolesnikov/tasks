from .models import ToDo, Category, Tag, ToDoTag
from .repositories.todo_repository import ToDoRepository
from .repositories.category_repository import CategoryRepository
from .repositories.tag_repository import TagRepository
from .repositories.todo_tag_repository import ToDoTagRepository

todo_repo = ToDoRepository()
category_repo = CategoryRepository()
tag_repo = TagRepository()
todo_tag_repo = ToDoTagRepository()


class ToDoService:
    @staticmethod
    def create(text, category, tags):
        todo = ToDo(text=text, category=category, tags=[])
        todo_id = todo_repo.insert(todo)
        inserted_todo = ToDoService.get(todo_id)
        ToDoService.set(todo=inserted_todo, tags_list=tags)
        return inserted_todo

    @staticmethod
    def update(todo, text, category, tags):
        todo.text = text
        todo.category = category
        todo_repo.update(todo)
        ToDoService.set(todo=todo, tags_list=tags)
        updated_todo = ToDoService.get(todo.id)
        return updated_todo

    @staticmethod
    def get_all():
        todos = []
        data = todo_repo.get_all()
        for todo_data in data:
            id, text, category_id = todo_data
            category = CategoryService.get(pk=category_id) if category_id else None
            todo = ToDo(id=id, text=text, category=category, tags=[])
            tags = ToDoTagService.get_by_todo(todo)
            todo.tags = tags
            todos.append(todo)
        return todos

    @staticmethod
    def get(pk):
        todo_data = todo_repo.get(pk=pk)
        if todo_data:
            id, text, category_id = todo_data
            category = CategoryService.get(pk=category_id) if category_id else None
            todo = ToDo(id=id, text=text, category=category, tags=[])
            tags = ToDoTagService.get_by_todo(todo)
            todo.tags = tags or []
            return todo
        else:
            return None

    @staticmethod
    def delete(pk):
        todo_repo.delete(pk=pk)

    @staticmethod
    def set(todo, tags_list):
        for tag in tags_list:
            if tag.id not in [tag.id for tag in todo.tags]:
                todo_tag_repo.insert(ToDoTag(todo_id=todo.id, tag_id=tag.id))
        for tag in todo.tags:
            if tag.id not in [tag.id for tag in tags_list]:
                todo_tag_repo.delete(todo=todo, tag=tag)
        todo.tags = tags_list

    @staticmethod
    def get_data_from_validation(serializer, validated_data):
        category_data = serializer.initial_data['category']
        tags_data = serializer.initial_data['tags']
        tags_ids = list(set([tag['id'] for tag in tags_data]))
        tags = []
        if tags_data:
            tags = [TagService.get(pk=id) for id in tags_ids]
        category_id = category_data['id'] if category_data else None
        text = validated_data.get('text')
        category = CategoryService.get(pk=category_id)
        return {'category': category,
                'text': text,
                'tags': tags}


class CategoryService:
    @staticmethod
    def get(pk):
        data = category_repo.get(pk=pk)
        if data:
            id, name = data
            return Category(id=id, name=name)
        else:
            return None


class TagService:
    @staticmethod
    def get(pk):
        data = tag_repo.get(pk=pk)
        if data:
            id, name = data
            return Tag(id=id, name=name)
        else:
            return None


class ToDoTagService:
    @staticmethod
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
