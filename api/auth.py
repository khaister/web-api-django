import base64

from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()


class AsyncBasicAuthentication(BaseAuthentication):
    keyword = "Basic"

    async def authenticate(self, request):
        auth = request.headers.get("Authorization")
        if not auth:
            raise AuthenticationFailed()

        if not auth.startswith(self.keyword):
            raise AuthenticationFailed()

        token = auth[len(self.keyword) :].strip()
        token = base64.b64decode(token).decode("utf-8")
        username, password = token.split(":")

        try:
            user = await User.objects.aget(username=username)
            valid_password = user.check_password(password)
            if not valid_password:
                raise AuthenticationFailed()
            return user, None
        except User.DoesNotExist:
            raise AuthenticationFailed()

    def authenticate_header(self, request):
        return self.keyword
