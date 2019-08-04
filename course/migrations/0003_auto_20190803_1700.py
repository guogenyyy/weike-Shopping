# Generated by Django 2.1.1 on 2019-08-03 09:00

import course.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20190803_0938'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '课程种类表', 'verbose_name_plural': '课程种类表'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': '课程表', 'verbose_name_plural': '课程表'},
        ),
        migrations.AlterField(
            model_name='course',
            name='createDatetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 3, 17, 0, 51, 393018), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='course',
            name='fileName',
            field=models.FileField(upload_to=course.models.save_file, verbose_name='文件名称'),
        ),
        migrations.AlterField(
            model_name='course',
            name='imgName',
            field=models.ImageField(upload_to=course.models.save_img, verbose_name='课程图片'),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='售价'),
        ),
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, '收费'), (1, '免费')], default=0, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='course',
            name='summary',
            field=models.CharField(blank=True, default='', max_length=1000, verbose_name='课程介绍'),
        ),
        migrations.AlterField(
            model_name='course',
            name='userBuyer',
            field=models.ManyToManyField(blank=True, related_name='userBuyer', to='user.User', verbose_name='购买用户'),
        ),
        migrations.AlterField(
            model_name='course',
            name='userShoppingcart',
            field=models.ManyToManyField(blank=True, related_name='userShoppingcart_set', to='user.User', verbose_name='加入购物车用户'),
        ),
    ]
