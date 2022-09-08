import json

from kakao import Kakao
from naver import Naver
from menu import get_foods_list

kakao = Kakao()
naver = Naver()

foods_list = get_foods_list()
template = naver.naver_searh("서면", foods_list)
kakao.send_kakao_message_to_self(template)
