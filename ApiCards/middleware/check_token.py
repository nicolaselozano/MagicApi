from functools import wraps
import re
import requests
from django.http import HttpRequest
from dotenv import load_dotenv
from jwt import PyJWKClient, InvalidTokenError
from rest_framework.response import Response
from rest_framework import status
import os

load_dotenv()

def check_token(view_func):

    @wraps(view_func)
    def _wrapped_view(request: HttpRequest, *args, **kwargs):
        try:
            CLIENT_ID = os.getenv('CLIENT_ID')
            CLIENT_SECRET = os.getenv('CLIENT_SECRET')
            REDIRECT_URL = os.getenv('REDIRECT_URL')
            DOMAIN = os.getenv('DOMAIN')
            AUDIENCE = os.getenv('AUDIENCE')

            h_token = request.headers.get('Authorization')
            if not h_token:
                return Response({"error": "Authorization header missing"}, status=status.HTTP_401_UNAUTHORIZED)

            regex_bearer = re.compile(r"^[Bb]earer (.*)$")
            match = regex_bearer.match(h_token)

            if not match:
                return Response({"error": "Invalid token format"}, status=status.HTTP_401_UNAUTHORIZED)

            token = match.group(1)

            jwks_client = get_signing_keys(DOMAIN)
            signing_key = jwks_client.get_signing_key_from_jwt(token)

            validation_options = {
                "verify_signature": True,
                "verify_aud": True,
                "verify_iss": True,
            }

            decoded_token = jwt.decode(
                token,
                signing_key.key,
                algorithms=["RS256"],
                audience=AUDIENCE,
                options=validation_options
            )

            print(f"El token es válido!", decoded_token)
            return view_func(request, *args, **kwargs)

        except InvalidTokenError:
            return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            return Response({"error": f"Token validation error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return _wrapped_view


def get_signing_keys(auth_domain):
    well_known_url = f"https://{auth_domain}/.well-known/openid-configuration"
    response = requests.get(well_known_url)
    openid_config = response.json()
    jwks_uri = openid_config["jwks_uri"]
    jwks_client = PyJWKClient(jwks_uri)
    return jwks_client
