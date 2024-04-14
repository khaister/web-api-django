import pdb

from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()


class AsyncAuthentication(BaseAuthentication):
    keyword = "Bearer"

    async def authenticate(self, request):
        auth = request.headers.get("Authorization")
        if not auth:
            return None

        if not auth.startswith(self.keyword):
            return None

        token = auth[len(self.keyword) :].strip()

        try:
            user = await User.objects.aget(token=token)
            return user, None
        except User.DoesNotExist:
            raise AuthenticationFailed("No such user")

    def authenticate_header(self, request):
        return self.keyword
