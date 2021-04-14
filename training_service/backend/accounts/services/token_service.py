import jwt
from django.contrib.auth.models import User
from rest_framework.generics import get_object_or_404

from training_service.settings import SECRET_KEY


def decode_token(token):
    decoded_token = jwt.decode(jwt=token,
                               algorithms='HS256',
                               key=SECRET_KEY)
    user = get_object_or_404(queryset=User.objects.all(), id=decoded_token['user_id'])
    return user
