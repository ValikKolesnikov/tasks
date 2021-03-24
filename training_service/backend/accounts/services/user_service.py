from django.contrib.auth.models import User


def create(username, email, first_name, last_name, password, groups):
    user = User(username=username, email=email, first_name=first_name, last_name=last_name)
    user.set_password(password)
    user.save()
    user.groups.set(groups)
    return user


def update(user, username=None, first_name=None, last_name=None, email=None, groups=None):
    if username:
        user.username = username
    if email:
        user.email = email
    if first_name:
        user.email = email
    if last_name:
        user.email = email
    user.save()
    if groups:
        user.groups.set(groups)
    return user
