import os
from functools import wraps
from http import client
from dotenv import load_dotenv

load_dotenv()
def set_token_middleware(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        CLIENT_ID = os.getenv('CLIENT_ID')
        CLIENT_SECRET = os.getenv('CLIENT_SECRET')
        REDIRECT_URL = os.getenv('REDIRECT_URL')
        DOMAIN = os.getenv('DOMAIN')

        code: str = str(request.GET.get('code'))

        conn = client.HTTPSConnection("")

        payload = (f"grant_type=authorization_code&"
                   f"client_id={CLIENT_ID}"
                   f"client_secret={CLIENT_SECRET}"
                   f"code={code}&"
                   f"redirect_uri={REDIRECT_URL}")

        headers = {'content-type': "application/x-www-form-urlencoded"}

        conn.request("POST", f"/{DOMAIN}/oauth/token", payload, headers)

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))
        return view_func(request, *args, **kwargs)

    return _wrapped_view
