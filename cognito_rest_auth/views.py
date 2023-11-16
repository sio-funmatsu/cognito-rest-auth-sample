from django.conf import settings
from pycognito import Cognito
from rest_framework.response import Response
from rest_framework.views import APIView

COGNITO_USER_POOL_ID = settings.COGNITO_USER_POOL_ID
COGNITO_CLIENT_ID = settings.COGNITO_CLIENT_ID
COGNITO_CLIENT_SECRET = settings.COGNITO_CLIENT_SECRET


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        cognito_client = Cognito(
            COGNITO_USER_POOL_ID,
            COGNITO_CLIENT_ID,
            client_secret=COGNITO_CLIENT_SECRET,
            username=username,
        )

        cognito_client.authenticate(password=password)

        return Response(
            {
                "access_token": cognito_client.access_token,
                "refresh_token": cognito_client.refresh_token,
            }
        )
