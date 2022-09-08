import copy
import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()


class Kakao():
  def __init__(self) -> object:
    self._kakao_rest_api = os.environ.get('KAKAO_REST_API')
    self._code = "BB6Lj48N-BkYz8rxtiBfekP1b2RcZiJN1xrEl4PFqJkyeBRY8xjv8vC9Z93JltAghMCqjQo9dRoAAAGDHHVc2Q"
    with open("kakao.json", "r") as fp:
      token = json.load(fp)
      if token.get('access_token'):
        self._access_token = token['access_token']

      if token.get('refresh_token'):
        self._refresh_token = token['refresh_token']
      else:
        pass

  def kakao_access_token(self):
    url = "https://kauth.kakao.com/oauth/token"
    redirect_uri = "https://localhost.com"
    data = {
      "grant_type": "authorization_code",
      "client_id": self._kakao_rest_api,
      "redirect_uri": redirect_uri,
      "code": self._code
    }

    res = requests.post(url, data=data)
    token = res.json()
    if "access_token" in token:
      with open("kakao.json", "w") as fp:
        json.dump(token, fp)
    else:
      print(res.status_code)

  def kakao_refresh_token(self):
    url = "https://kauth.kakao.com/oauth/token"
    data = {
      "grant_type": "refresh_token",
      "client_id": self._kakao_rest_api,
      "refresh_token": self._refresh_token,
    }

    res = requests.post(url, data=data)
    token = res.json()
    if "access_token" in token:
      with open("kakao.json", "w") as fp:
        json.dump(token, fp)
    else:
      print(res.status_code)

  def send_kakao_message_to_self(self, template):
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    header = {
      "Authorization": f"Bearer {self._access_token}"
    }

    data = {
      'template_object': json.dumps(template, ensure_ascii=False)
    }
    res = requests.post(url, headers=header, data=data)
    print(res.status_code)
    if res.json().get('result_code') == 0:
      print("SUCCESS SENDING TO MESSAGE 💌")
    else:
      print(f"FAIL TO SENDING TO MESSAGE, {res.status_code}-{res.json()}")
