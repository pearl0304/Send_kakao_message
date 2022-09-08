import json
import os
import requests
from dotenv import load_dotenv
import urllib

load_dotenv()


class Naver():
  def __init__(self):
    self._naver_client = os.environ.get('NAVER_CLIENT_ID')
    self._naver_client_secret = os.environ.get('NAVER_CLIENT_SECRET')
    self.header = {
      "X-Naver-Client-ID": self._naver_client,
      "X-Naver-Client-Secret": self._naver_client_secret
    }

  def naver_searh(self, search_location, foodlist):
    naver_local_url = "https://openapi.naver.com/v1/search/local.json?"
    location = search_location
    recommends = []
    contents = []

    for food in foodlist:
      query = f"{location}{food} 맛집"
      params = f"sort=comment&query={query}&display=5"

      res = requests.get(f"{naver_local_url}{params}", headers=self.header)
      result_list = res.json().get('items')

      if result_list:
        recommends.append(result_list[0])
        if len(recommends) >= 3:
          break

    for place in recommends:
      title = place.get('title')
      title = title.replace('<b>', '').replace('</b>', '')
      category = place.get('category')
      telephone = place.get('telephone')
      roadAddress = place.get('roadAddress')

      ## Connect to naver search when click the place
      enc_address = urllib.parse.quote(f"{roadAddress} {title}")
      query = f"query={enc_address}"

      if '카페' in category:
        image_url = "https://freesvg.org/img/pitr_Coffee_cup_icon.png"
      else:
        image_url = "https://freesvg.org/img/bentolunch.png?w=150&h=150&fit=fill"

      if telephone:
        title = f"{title} tel {telephone}"

      content = {
        "title": f"[{category}] {title}",
        "description": ' '.join(roadAddress.split()[1:]),
        "image_url": image_url,
        "image_width": 50,
        "image_height": 50,
        "link": {
          "web_url": f"https://search.naver.com/search.naver?{query}",
          "mobile_web_url": f"https://search.naver.com/search.naver?{query}"
        }
      }
      contents.append(content)

    template = {
      "object_type": "list",
      "header_title": "메뉴 랜덤 추천",
      "header_link": {
        "web_url": "https://naver.com",
        "mobile_web_url": "https://naver.com"
      },
      "contents": contents
    }
    return template
