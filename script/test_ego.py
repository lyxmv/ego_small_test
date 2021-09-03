import unittest
import logging
import app
from api.ego_api import EgoApi
class TestEgo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.ego_api = EgoApi()
    def test01_get_banner_success(self):
        response = self.ego_api.get_banner()
        logging.info("获取轮播图结果为:{}".format(response.json()))
        self.assertEqual(200,response.status_code)
    def test02_get_theme_success(self):
        response = self.ego_api.get_theme("ids=1,2,3")
        logging.info("获取主题栏位结果为:{}".format(response.json()))
        self.assertEqual(200, response.status_code)
        self.assertEqual("美味水果世界",response.json()[0].get("description"))
    def test03_get_recent_goods(self):
        response = self.ego_api.get_recent_goods()
        logging.info("获取最近新品结果为:{}".format(response.json()))
        self.assertEqual(200,response.status_code)
        self.assertIn("梨花带雨",response.json()[1].get("name"))
    def test04_get_product_category(self):
        response = self.ego_api.get_prduct_category()
        logging.info("获取商品分类结果为:{}".format(response.json()))
        self.assertEqual(200,response.status_code)
        self.assertEqual("炒货",response.json()[2].get("name"))

    def test05_by_category(self):
        response = self.ego_api.by_category_goods("id=2")
        logging.info("获取商品分类下的商品结果为:{}".format(response.json()))
        self.assertEqual(200,response.status_code)
        self.assertEqual(2,response.json()[0].get("id"))
    def test06_product_detail_good(self):
        response = self.ego_api.get_product_details_goods(7)
        logging.info("获取商品分类下的商品详细结果为:{}".format(response.json()))
        self.assertEqual(200,response.status_code)
        self.assertEqual("泥蒿 半斤",response.json().get("name"))

    def test07_get_token(self):
        response = self.ego_api.get_token(app.HEADERS,
                                          {"code":"021Ct8000GLeiM17Ri100jSnDH1Ct809"},
                                          )
        logging.info("获取token结果为:{}".format(response.json()))
        logging.info("response.json().get('token')：{}.".format(response.json().get("token")))
        self.assertTrue(response.json().get("token"))
    def test08_verify_token(self):
        response = self.ego_api.verify_token(app.HEADERS,
                                            {"token":"173287596229c2835052fddb224f5398"}
                                             )
        logging.info("验证token结果为:{}".format(response.json()))
        self.assertEqual(200,response.status_code)
        self.assertTrue(response.json().get("isValid"))
    def test09_get_user_list(self):
        app.HEADERS["token"]="9df2cba9ab58f6d3ae21b6b548fd6aa0"
        response = self.ego_api.get_user_list(app.HEADERS, "page=1")
        logging.info("获取用户订单结果为:{}".format(response.json()))
        self.assertEqual(200,response.status_code)
        self.assertIn("夏日芒果",response.json().get('data')[0].get("snap_name"))
    def test10_create_list(self):
        app.HEADERS["token"] = "9df2cba9ab58f6d3ae21b6b548fd6aa0"
        response = self.ego_api.create_list(app.HEADERS,
                                            {"products":[{"product_id":8,"count":1}]}
                                            )
        logging.info("创建订单结果为:{}".format(response.json()))
        self.assertEqual(200,response.status_code)
        self.assertEqual(True,response.json().get("pass"))
    def test11_see_list(self):
        app.HEADERS["token"] = "9df2cba9ab58f6d3ae21b6b548fd6aa0"
        response =self.ego_api.check_list(app.HEADERS,50)
        logging.info("查看订单结果为:{}".format(response.json()))
        self.assertEqual(200, response.status_code)
        self.assertEqual(50,response.json().get("id"))
    def test12_get_address(self):
        app.HEADERS["token"] = "9df2cba9ab58f6d3ae21b6b548fd6aa0"
        response = self.ego_api.get_address(app.HEADERS)
        logging.info("获取地址结果为:{}".format(response.json()))
        self.assertEqual(200, response.status_code)
        self.assertEqual("张三",response.json().get("name"))
