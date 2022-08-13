from dataclasses import asdict

from api.session_http_api import SessionHttpApi
from framework.http import HttpRequest
from model.goods import Goods
from model.goods_api import GoodsApi
from model.oauth import Oauth
from utils.logger import logger


class GoodHttpApi(GoodsApi):
    def listGoods(self, searchName, page=1, limit=10):
        http_req = HttpRequest()
        http_req.method = 'GET'
        http_req.path = "/wx/goods/list"
        http_req.headers['X-Litemall-Token'] = SessionHttpApi().refresh_token(oauth=Oauth())
        http_req.query = {'keyword': searchName, 'page': page, 'limit': limit}
        res = http_req.send()
        logger.info("获取商品列表的返回值：{}".format(res.json()))
        # if res.json()['errno'] == 0:
        #     return res.json()['data']['list']
        # else:
        #     return res
        goodList = []
        good = Goods()
        if res.json()['errno'] == 0:
            if res.json()['data']['total'] != 0:
                for item in res.json()['data']['list']:
                    good.id = item['id']
                    good.name = item['name']
                    good.retailPrice = item['retailPrice']
                    goodList.append(asdict(good))
                return goodList
            else:
                return res.json()['data']['list']
        else:
            return res

    def getGoodDetails(self, goodId):

        http_req = HttpRequest()
        http_req.method = 'GET'
        http_req.path = "/wx/goods/detail"
        http_req.headers['X-Litemall-Token'] = SessionHttpApi().refresh_token(oauth=Oauth())
        http_req.query = {'id': goodId}
        # http_req.json = {'id': goodId}
        res = http_req.send()
        logger.info("商品详情返回值：{}".format(res.json()))
        # logger.info("商品的productId:{}".format(res.json()['data']))
        # logger.info("商品的productId:{}".format(res.json()['data']['productList']))
        # logger.info("商品的productId:{}".format(res.json()['data']['productList'][0]['id']))
        return res

