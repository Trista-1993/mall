import json

from framework.http import HttpRequest
from model.oauth import Oauth
from model.session import Session
import requests
import json

from utils.logger import logger


class SessionHttpApi(Session):
    # logger.info("json值：{}".format(json))

    def refresh_token(self, oauth: Oauth):
        # res = requests.post(
        #     'https://litemall.hogwarts.ceshiren.com/wx/auth/login',
        #     json={'username': username, 'password': password}
        # )
        http_req = HttpRequest()
        http_req.method = 'POST'
        http_req.path = "/wx/auth/login"
        http_req.json = {'username': oauth.username, 'password': oauth.password}
        res = http_req.send()

        logger.info("获取token的返回值：{}".format(res.json()))
        logger.info("token is ：{}".format(res.json()['data']['token']))
        return res.json()['data']['token']




if __name__ == '__main__':
    a = SessionHttpApi()
    oauth = Oauth
    r = a.refresh_token(oauth)
    print("token is :{}".format(r))
