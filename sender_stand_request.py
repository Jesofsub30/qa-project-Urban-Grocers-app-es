import configuration as C
import configuration
import requests

import data
from data import user_body, headers, kit_body


def post_new_user(body):
    return requests.post(C.URL_SERVICE+C.CREATE_USER_PATH,
                  json=user_body,
                  headers=data.headers)

response = post_new_user(data.user_body);



def post_new_client_kit(kit_body):
    create_user = post_new_user(data.user_body)
    auth_token = post_new_user(data.headers_new_kit).json()["authToken"]
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    return requests.post(C.URL_SERVICE+C.KITS_PATH,
                         json = kit_body,
                         headers = headers)

