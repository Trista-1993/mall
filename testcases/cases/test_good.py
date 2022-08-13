from dataclasses import asdict

import allure

from api.good_http_api import GoodHttpApi
from api.session_http_api import SessionHttpApi
import pytest

from model.oauth import Oauth
from utils.ReadFile import Api_Data
from utils.logger import logger


class TestGood:

    def setup_class(self):
        oauth = Oauth()
        self.session = SessionHttpApi().refresh_token(oauth)

        # good初始化
        self.good = GoodHttpApi()

    def teardown_class(self):
        ...

    def setup(self):
        ...

    def teardown(self):
        ...

    @allure.story("用例1：查看商品列表")
    @allure.severity('normal')
    @pytest.mark.parametrize("searchName", [""])
    def test_good_list(self, searchName):
        res = self.good.listGoods(searchName)
        logger.info("查看商品列表: {}".format(res))
        assert len(res) >= 0

    @allure.story("用例2：搜索商品")
    @allure.severity('normal')
    @pytest.mark.parametrize("searchName", ['3D', "3D@@"])
    def test_good_search(self, searchName):
        res = self.good.listGoods(searchName)
        logger.info("搜索{}开头的商品: {}".format(searchName, res))
        assert len(res) >= 0

    @allure.story("用例3：查看商品详情")
    @allure.severity('normal')
    @pytest.mark.parametrize("goodid, errno, errmsg", Api_Data['test_good_detail'])
    def test_good_detail(self, goodid, errno, errmsg):
        res = self.good.getGoodDetails(goodid)
        if res.json()['errno'] == 0:
            assert res.json()['errno'] == errno
            assert res.json()['errmsg'] == errmsg
            assert "3D" in res.json()['data']['info']['name']
        else:
            assert res.json()['errno'] == errno
            assert res.json()['errmsg'] == errmsg

