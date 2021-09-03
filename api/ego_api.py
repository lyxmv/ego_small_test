import app
import requests

class EgoApi:
    def __init__(self):
        self.banner_url = app.BASE_URL+"/api/v1/banner/1"
        self.theme_url = app.BASE_URL+"/api/v1/theme"
        self.recent_goods_url = app.BASE_URL+"/api/v1/product/recent"
        # 获取商品分类url
        self.get_category_url = app.BASE_URL + "/api/v1/category/all"
        # 获取商品分类下的某个商品
        self.by_category_url = app.BASE_URL+ "/api/v1/product/by_category"
        # 获取商品详情
        self.product_detail_url = app.BASE_URL+ "/api/v1/product/"
        self.token_url = app.BASE_URL+"/api/v1/token/user"
        self.address_url = app.BASE_URL+"/api/v1/address"
        self.verify_token_url = app.BASE_URL+"/api/v1/token/verify"
        self.get_user_good_url = app.BASE_URL+"/api/v1/order/by_user"
        self.creat_list_url = app.BASE_URL+"/api/v1/order"
        self.see_list_url = app.BASE_URL+"/api/v1/order"

    def get_banner(self):
        return requests.get(url = self.banner_url)
    def get_theme(self,id):
        url = self.theme_url + "?" + id
        return requests.get(url = url)
    def get_recent_goods(self):
        return requests.get(url = self.recent_goods_url)
    def get_prduct_category(self):
        return requests.get(url = self.get_category_url)
    def by_category_goods(self,ids):
        url = self.by_category_url + "?" + ids
        return requests.get(url=url)
    def get_product_details_goods(self,id):
        url = self.product_detail_url + "/" + str(id)
        return requests.get(url=url)
    def get_token(self,headers,json):
        return requests.post(self.token_url,headers=headers,json=json)
    def verify_token(self,headers,json):
        return requests.post(self.verify_token_url,headers=headers,json=json)
    def get_user_list(self,headers,page):
        # url = self.get_user_good_url + "?" + str(page)
        return requests.get(url=self.get_user_good_url, headers=headers, params=page)
    def create_list(self,headers,json):
        return requests.post(self.creat_list_url,headers=headers,json=json)
    def check_list(self,headers,id):
        url = self.see_list_url + "/" +str(id)
        return requests.get(url=url,headers=headers)
    def get_address(self,headers):
        return requests.get(self.address_url,headers=headers)