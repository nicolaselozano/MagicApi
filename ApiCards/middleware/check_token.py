from functools import wraps
import re
import requests
import jwt
from django.http import HttpRequest
from dotenv import environ
from jwt import PyJWKClient, InvalidTokenError

env = environ.Env()
environ.Env.read_env()
CLIENT_ID = environ.get('CLIENT_ID')
CLIENT_SECRET = environ.get('CLIENT_SECRET')
REDIRECT_URL = environ.get('REDIRECT_URL')
DOMAIN = environ.get('DOMAIN')
AUDIENCE = environ.get('AUDIENCE')


def check_token(view_func):
    @wraps(view_func)
    def _wrapped_view(request: HttpRequest, *args, **kwargs):
        try:
            h_token = request.headers.get('Authorization')
            regex_bearer = re.compile(r"^[Bb]earer (.*)$")

            existToken = regex_bearer.match(h_token)

            if existToken:
                token = existToken.group(1)
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
            print(f"El token es valido!")
            return decoded_token

        except InvalidTokenError as ex:
            print(f"Token inválido: {ex}")
            return None
        except Exception as ex:
            print(f"Error inesperado: {ex}")
            return None


def get_signing_keys(auth_domain):
    well_known_url = f"https://{auth_domain}/.well-known/openid-configuration"
    response = requests.get(well_known_url)
    openid_config = response.json()
    jwks_uri = openid_config["jwks_uri"]
    jwks_client = PyJWKClient(jwks_uri)
    return jwks_client
