from api.session_http_api import SessionHttpApi
from framework.http import HttpRequest
from model.cart import Cart
from model.cart_api import CartApi
from model.oauth import Oauth
from utils.logger import logger


class CartHttpApi(CartApi):

    def cartAdd(self, goodsId, productId, number):
        http_req = HttpRequest()
        http_req.method = 'POST'
        http_req.path = "/wx/cart/add"
        http_req.headers['X-Litemall-Token'] = SessionHttpApi().refresh_token(oauth=Oauth())
        http_req.json = {"goodsId": goodsId, "number": number, "productId": productId}
        res = http_req.send()
        logger.info("获取商品列表的返回值：{}".format(res.json()))
        return res

    def cartIndex(self):
        cartList = []
        cartGood = Cart()
        http_req = HttpRequest()
        http_req.method = 'GET'
        http_req.path = "/wx/cart/index"
        http_req.headers['X-Litemall-Token'] = SessionHttpApi().refresh_token(oauth=Oauth())
        res = http_req.send()
        # for item in res.json()['data']['cartList']:
        #     cartGood.goodsId = item['goodsId']
        #     cartGood.goodsName = item['goodsName']
        #     cartGood.number = item['number']
        #     cartGood.productId = item['productId']

        # cartList.append(cartGood)
        return res

        # logger.info("购物车列表：{}".format(cartList))

    def cartDelete(self):
        ...
