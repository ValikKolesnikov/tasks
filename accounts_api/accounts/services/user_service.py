from django.contrib.auth.models import User, Group


def get_data_from_validated_data(serializer, validated_data):
    pass


def create(username, email, password, groups_data):
    user = User(username=username, email=email)
    groups = [Group.objects.get(id=group['id']) for group in groups_data]
    user.set_password(password)
    user.save()
    user.groups.set(groups)
    return user


def update(user, username, email, groups_data):
    if username:
        user.username = username
    if email:
        user.email = email
    user.save()
    if groups_data:
        groups = [Group.objects.get(id=group['id']) for group in groups_data]
        user.groups.set(groups)
    return user
