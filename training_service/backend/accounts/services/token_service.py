import jwt
from django.contrib.auth.models import User
from rest_framework.generics import get_object_or_404
from training_service.settings import SECRET_KEY


def get_user_token(user):
    token_payload = {
        'user_id': user.id
    }

    token = jwt.encode(payload=token_payload,
                       algorithm='HS256',
                       key=SECRET_KEY).decode(encoding='utf-8')
    return token


def decode_token(token):
    decoded_token = jwt.decode(jwt=token,
                               algorithms='HS256',
                               key=SECRET_KEY)
    user = get_object_or_404(queryset=User.objects.all(), id=decoded_token['user_id'])
    return user
