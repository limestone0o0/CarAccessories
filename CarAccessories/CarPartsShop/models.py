# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CarnewsCarnews(models.Model):
    news_title = models.CharField(max_length=50, blank=True, null=True)
    news_time_str = models.CharField(max_length=20, blank=True, null=True)
    news_art_time = models.CharField(max_length=32, blank=True, null=True)
    news_list_img = models.CharField(max_length=100, blank=True, null=True)
    news_path = models.CharField(max_length=100, blank=True, null=True)
    news_read_num = models.CharField(max_length=20, blank=True, null=True)
    news_comment_num = models.CharField(max_length=20, blank=True, null=True)
    news_abstract = models.TextField(blank=True, null=True)
    news_art_img = models.TextField(blank=True, null=True)
    news_art_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CarNews_carnews'


class CarpartsshopCarparts(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    img = models.CharField(max_length=512, blank=True, null=True)
    price = models.CharField(max_length=32, blank=True, null=True)
    grade = models.CharField(max_length=32, blank=True, null=True)
    comment_number = models.CharField(max_length=32, blank=True, null=True)
    brand = models.CharField(max_length=32, blank=True, null=True)
    shop_feature = models.CharField(max_length=512, blank=True, null=True)
    type = models.ForeignKey('CarpartsshopCartype', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CarPartsShop_carparts'


class CarpartsshopCartype(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    img = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CarPartsShop_cartype'


class UserRegister(models.Model):
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=32)



class Userinfo(models.Model):
    email = models.CharField(max_length=254)
    username = models.CharField(max_length=32)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=256)
    description = models.CharField(max_length=512)


class Cart(models.Model):
    shops_id = models.IntegerField(null=False)
    name = models.CharField(max_length=128, null=True)
    img = models.CharField(max_length=512, null=True)
    price = models.CharField(max_length=32, null=True)
    shops_num = models.IntegerField(null=False)
    shops_total_price = models.IntegerField(null=False)


class RelationsCartUserInfo(models.Model):
    userinfo_id = models.IntegerField()
    cart_id = models.IntegerField()


class ShopsOrder(models.Model):
    od_id = models.IntegerField()
    od_shops_names = models.CharField(max_length=2048)
    od_status = models.IntegerField()
    user_name = models.CharField(max_length=256, null=True)
    od_shops_nums = models.IntegerField(null=False)
    od_time = models.DateTimeField(null=False)
    od_shops_total_price = models.IntegerField(null=False)
