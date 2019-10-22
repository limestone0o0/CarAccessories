# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

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


class CarpartsshopRegisteruser(models.Model):
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'CarPartsShop_registeruser'


class CarpartsshopUserinfo(models.Model):
    email = models.CharField(max_length=254)
    username = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'CarPartsShop_userinfo'


