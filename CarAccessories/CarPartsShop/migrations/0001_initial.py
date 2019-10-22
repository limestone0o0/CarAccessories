# Generated by Django 2.1.8 on 2019-10-22 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarpartsshopCarparts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('img', models.CharField(blank=True, max_length=512, null=True)),
                ('price', models.CharField(blank=True, max_length=32, null=True)),
                ('grade', models.CharField(blank=True, max_length=32, null=True)),
                ('comment_number', models.CharField(blank=True, max_length=32, null=True)),
                ('brand', models.CharField(blank=True, max_length=32, null=True)),
                ('shop_feature', models.CharField(blank=True, max_length=512, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'CarPartsShop_carparts',
            },
        ),
        migrations.CreateModel(
            name='CarpartsshopCartype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('img', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'CarPartsShop_cartype',
            },
        ),
        migrations.CreateModel(
            name='CarpartsshopRegisteruser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=254)),
                ('password', models.CharField(max_length=32)),
            ],
            options={
                'managed': False,
                'db_table': 'CarPartsShop_registeruser',
            },
        ),
        migrations.CreateModel(
            name='CarpartsshopUserinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=254)),
                ('username', models.CharField(max_length=32)),
            ],
            options={
                'managed': False,
                'db_table': 'CarPartsShop_userinfo',
            },
        ),
    ]
