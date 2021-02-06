from todos.models import Category
from todos.repositories.category_repository import CategoryRepository

category_repo = CategoryRepository()


def get(pk):
    data = category_repo.get(pk=pk)
    if data:
        id, name = data
        return Category(id=id, name=name)
    else:
        return None
