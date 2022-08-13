import json
from dataclasses import dataclass, field
from utils.logger import logger
from utils.ReadFile import Config_Data

import requests
from requests import Response as RequestsResponse

@dataclass
class HttpRequest:
    method: str = None
    host: str = None
    path: str = None
    query: dict = None
    headers: dict = field(default_factory=dict)
    type: str = 'json'
    data: dict = None
    json: dict = None

    def send(self):

        # 多套环境
        self.host = Config_Data['mall']['url']

        # logger.info(type(self.host))

        # token处理
        # self.headers['token'] = ''

        if self.type == 'json':
            self.headers['Content-type'] = 'application/json'
            if self.data is not None:
                self.data = json.dumps(self.data)
            # if self.json is not None:
            #     self.json = json.dumps(self.json)

        elif self.type == 'xml':
            ...
        else:
            raise Exception('not exist format' + self.type)

        logger.info("send: {}".format(self))
        requests_response = requests.request(
            method=self.method,
            url=self.host + self.path,
            params=self.query,
            headers=self.headers,
            data=self.data,
            json=self.json,
            auth=None,
            # proxies={
            #     "http": 'http://127.0.0.1:8080',
            #     "https": 'http://127.0.0.1:8080'
            # },
            verify=False
        )
        logger.info("url:{}".format(self.host))
        logger.info("path:{}".format(self.path))
        res = HttpResponse(requests_response)
        logger.info("res.json {}".format(res.json()))
        return res


@dataclass()
class HttpResponse:
    def __init__(self, requests_response):
        self.res: RequestsResponse = requests_response

    def json(self):
        return self.res.json()

    # 解密
    def data(self) -> dict:
        pass
        # return json.loads(base64.decode(self.res.text))

    @property
    def status_code(self):
        return self.res.status_code
