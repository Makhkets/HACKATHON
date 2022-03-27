from django.contrib.auth.hashers import make_password
from api.v1.users.serializers import CreateUserSerializer, TokenSerializer
from utils.utils import validate_password, get_token


def create_user_and_tokens(ctx, request):
    temp_data = {
        'name': request.data["name"],
        'email': request.data["email"],
        'password': validate_password(ctx, request.data["password"])
    }
    serializer = CreateUserSerializer(data=temp_data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token_data = {
        'confirmation_token': get_token(),
        'reset_password_token': get_token(),
        'phone_auth_code': get_token(4, only_digits=True),
        'user': user.id
    }
    token_serializer = TokenSerializer(data=token_data)
    token_serializer.is_valid(raise_exception=True)
    tokens = token_serializer.save()
    return tokens, user


def auto_registrate_user(email, name=None, password=None, extra_data={}):
    if not password:
        password = get_token(length=6)

    if not name:
        name = email

    temp_data = {
        'name': name,
        'email': email,
        'password': make_password(password)
    }
    serializer = CreateUserSerializer(data=temp_data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token_data = {
        'confirmation_token': get_token(),
        'reset_password_token': get_token(),
        'phone_auth_code': get_token(4, only_digits=True),
        'user': user.id
    }
    token_serializer = TokenSerializer(data=token_data)
    token_serializer.is_valid(raise_exception=True)
    tokens = token_serializer.save()
    # send_auto_registrate_info.apply_async(args=[email, password, extra_data])
    return user
