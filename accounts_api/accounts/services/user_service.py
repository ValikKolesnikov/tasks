from django.contrib.auth.models import User


def create(username, email, password, groups):
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()
    user.groups.set(groups)
    return user


def update(user, username, email, groups):
    if username:
        user.username = username
    if email:
        user.email = email
    user.save()
    if groups:
        user.groups.set(groups)
    return user
