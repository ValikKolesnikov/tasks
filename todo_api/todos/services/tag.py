from todos.models import Tag
from todos.repositories.tag_repository import TagRepository

tag_repo = TagRepository()


def get(pk):
    data = tag_repo.get(pk=pk)
    if data:
        id, name = data
        return Tag(id=id, name=name)
    else:
        return None
