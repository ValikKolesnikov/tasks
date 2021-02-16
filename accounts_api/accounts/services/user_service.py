from django.contrib.auth.models import User, Group


def create(username, email, password, group_ids):
    user = User(username=username, email=email)
    groups = Group.objects.prefetch_related('permissions').filter(id__in=group_ids)
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
        group_ids = [group['id'] for group in groups_data]
        user.groups.set(Group.objects.prefetch_related('permissions').filter(id__in=group_ids))
    return user


