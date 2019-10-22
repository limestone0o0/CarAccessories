from lxml import etree
from sqlalchemy import *
from functools import reduce
from sqlalchemy.orm import sessionmaker,relationship,backref
from sqlalchemy.ext.declarative import declarative_base


import requests
import sqlalchemy


db = sqlalchemy.create_engine('mysql+pymysql://root:7890@39.107.253.135:33060/carparts?charset=utf8')
base = declarative_base(db)


class CarType(base):
    __tablename__ = 'CarPartsShop_cartype'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(32),default='1')
class CarParts(base):
    __tablename__ = 'CarPartsShop_carparts'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(128),default='1')
    img = sqlalchemy.Column(sqlalchemy.String(512),default='1')
    price = sqlalchemy.Column(sqlalchemy.String(32),default='1')
    grade = sqlalchemy.Column(sqlalchemy.String(32),default='1')
    comment_number = sqlalchemy.Column(sqlalchemy.String(32),default='1')
    brand = sqlalchemy.Column(sqlalchemy.String(32),default='1')
    shop_feature = sqlalchemy.Column(sqlalchemy.String(512),default='1')
    type_id = sqlalchemy.Column(sqlalchemy.Integer,ForeignKey(CarType.id))
    CarPartsShop_cartype = relationship('CarType',backref = 'CarPartsShop_carparts')
proxies = {
    'http':'163.125.249.79:8118'
}
headers = {
    'user-agent':'dsdsdsdsadd'
}
session = sessionmaker(bind=db)
session = session()
url = 'https://item.tuhu.cn/Search.html?s='#基础url
#获取商品列表的url地址，爬取图片 价格  名字  评分  评论人数
def get_list_tree(url,name):

    url = url + name
    response = requests.get(url,headers=headers)
    content = response.content.decode('utf-8')
    tree = etree.HTML(content)
    return tree


#获取到brand的列表
def get_brand(url,name):
    tree = get_list_tree(url,name)
    detail_url_list = tree.xpath('//tr/td[@class="td2"]/a/@href')
    brand_list = []
    for url in detail_url_list:
        content = requests.get(url,headers=headers).content.decode('utf-8')
        tree = etree.HTML(content)
        brand = tree.xpath('//div[@class="properties"]/ul/li/text()')
        brand_list.append(brand[0])
    return brand_list

#获取到特点图片的列表
def get_shopfeature(url,name):
    tree = get_list_tree(url,name)
    detail_url_list = tree.xpath('//tr/td[@class="td2"]/a/@href')
    shop_feature_list = []
    for url in detail_url_list:
        content = requests.get(url,headers=headers).content.decode('utf-8')
        tree = etree.HTML(content)
        feature_list = tree.xpath('//p[@style="text-align: center"]/img/@src')
        shop_feature = reduce(lambda x, y: x + '|' + y, feature_list[0:4])
        shop_feature_list.append(shop_feature)
    return shop_feature_list

#获取到名字的列表
def get_name(name_list):
    new_name_list = []
    for old_name in name_list:
        name = old_name.strip()
        if name != '':
            new_name_list.append(name)
    return new_name_list


# def get_price(price_list):
#     new_price_list = []
#     for price in price_list:
#         price = price[1:]
#         new_price_list.append(price)
#     return new_price_list



if __name__ == '__main__':
    name = '玻璃水'
    tree = get_list_tree(url,name)
    name_list = tree.xpath('//tr/td[@class="td2"]/a/text()')
    new_name_list = get_name(name_list)
    # img_list = tree.xpath('//tr/td[@class="td1"]/a/img/@src')
    # price_list = tree.xpath('//tr/td[@class="td3"]/div/strong/text()')
    # comment_number_list = tree.xpath('//tr/td[@class="td2"]/div/div/span/em/text()')
    # grade_list = tree.xpath('//tr/td[@class="td2"]/div/div/label[@class="scored"]/text()')
    # brand_list = get_brand(url,name)
    feature_list = get_shopfeature(url,name)
    # from sqlalchemy.orm import sessionmaker
    # session = sessionmaker(bind=db)
    # session = session()
    # for i in range(0,20):
    #     carcom = CarParts()
    #     carcom.name = new_name_list[i]
    #     carcom.img = img_list[i]
    #     carcom.price = price_list[i]
    #     carcom.grade = grade_list[i]
    #     carcom.comment_number = comment_number_list[i]
    #     carcom.brand = brand_list[i]
    #     carcom.shop_feature = feature_list[i]
    #     carcom.type_id = 5
    #     session.add(carcom)
    #     session.commit()
    # ct = CarType()
    # ct.name = name
    # session.add(ct)
    # session.commit()
    # base.metadata.create_all(db)

