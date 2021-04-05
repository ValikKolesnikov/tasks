from django.contrib.auth.models import User, Group


def create_user(username, email, first_name, last_name, password, group):
    user = User(username=username, email=email, first_name=first_name, last_name=last_name)
    user.set_password(password)
    user.save()
    user_group = None
    if group == 'teacher':
        user_group = Group.objects.get_or_create(name='Teacher')
    elif group == 'student':
        user_group = Group.objects.get_or_create(name='Student')
    user.groups.set([user_group[0]])
    return user


def update_user(user, username=None, first_name=None, last_name=None, email=None, group=None):
    if username:
        user.username = username
    if email:
        user.email = email
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name
    user.save()
    if group:
        user_group = None
        if group == 'teacher':
            user_group = Group.objects.get_or_create(name='Teacher')
        elif group == 'student':
            user_group = Group.objects.get_or_create(name='Student')
        user.groups.set([user_group[0]])
    return user
