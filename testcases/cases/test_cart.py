from dataclasses import asdict

import allure

from api.cart_http_api import CartHttpApi
from api.good_http_api import GoodHttpApi
from api.session_http_api import SessionHttpApi
import pytest

from model.oauth import Oauth
from utils.ReadFile import Api_Data
from utils.logger import logger


class TestCart:

    def setup_class(self):
        oauth = Oauth()
        self.session = SessionHttpApi().refresh_token(oauth)
        self.cart = CartHttpApi()

    def teardown_class(self):
        ...

    def setup(self):
        ...

    def teardown(self):
        ...

    @allure.story("用例1：添加商品到购物车")
    @allure.severity('critical')
    @pytest.mark.parametrize("goodid, productid, number,errno, errmg", Api_Data["test_cart_add"])
    def test_cart_add(self, goodid, productid, number, errno, errmg):
        res = self.cart.cartAdd(goodid, productid, number)
        if res.json()['errno'] == 0:
            logger.info("添加商品到购物车成功，请求响应为: {}".format(res.json()))
            assert res.json()['errno'] == errno
            assert res.json()['errmsg'] == errmg
        else:
            logger.info("添加商品到购物车失败，请求响应为: {}".format(res.json()))
            assert res.json()['errno'] == errno
            assert res.json()['errmsg'] == errmg

    def test_cart_index(self):
        res = self.cart.cartIndex()
        assert res.json()['errno'] == 0
