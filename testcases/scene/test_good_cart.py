import allure
import pytest

from api.cart_http_api import CartHttpApi
from api.good_http_api import GoodHttpApi
from api.session_http_api import SessionHttpApi
from model.oauth import Oauth
from utils.logger import logger


@allure.step("步骤1 ==>> 搜索商品")
def step_1():
    logger.info("步骤1 ==>> 搜索商品")


@allure.step("步骤2 ==>> 查看商品详情")
def step_2():
    logger.info("步骤2 ==>> 查看商品详情")


@allure.step("步骤3 ==>> 商品加入购物车")
def step_3():
    logger.info("步骤3 ==>> 商品加入购物车")


@allure.step("步骤4 ==>> 获取购物车列表")
def step_4():
    logger.info("步骤4 ==>> 获取购物车列表")


class TestList():

    def setup_class(self):
        oauth = Oauth()
        self.session = SessionHttpApi().refresh_token(oauth)

        # # good初始化
        self.good = GoodHttpApi()
        self.cart = CartHttpApi()

    def teardown_class(self):
        ...

    def setup(self):
        ...

    def teardown(self):
        ...

    @allure.story("用例1：搜索3D开头的商品")
    @allure.severity('critical')
    @pytest.mark.parametrize("searchName", ['3D'])
    def test_good_cart(self, searchName):
        step_1
        good_list = self.good.listGoods(searchName)
        good_id = good_list[0]['id']
        logger.info("搜索商品获取商品goodid: {}".format(good_id))

        step_2
        good_detail = self.good.getGoodDetails(good_id)
        product_id = good_detail.json()['data']['productList'][0]['id']
        logger.info("查看商品详情获取productid: {}".format(product_id))

        step_3
        add_cart = self.cart.cartAdd(good_id, product_id, number=1)
        logger.info("商品加入购物车响应:{}".format(add_cart.json()))

        step_4
        index_cart = self.cart.cartIndex()
        logger.info("获取购物车列表:{}".format(index_cart.json()))
        assert good_id == index_cart.json()['data']['cartList'][0]['goodsId']
        assert searchName in index_cart.json()['data']['cartList'][0]['goodsName']
