# Generated by Django 2.1.1 on 2019-08-03 01:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='课程种类')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=40, verbose_name='课程名称')),
                ('fileName', models.FileField(upload_to='', verbose_name='文件名称')),
                ('imgName', models.ImageField(upload_to='', verbose_name='课程图片')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='售价')),
                ('summary', models.CharField(default='', max_length=1000, verbose_name='课程介绍')),
                ('status', models.PositiveSmallIntegerField(default=0, verbose_name='状态')),
                ('createDatetime', models.DateTimeField(default=datetime.datetime(2019, 8, 3, 9, 23, 54, 315233))),
                ('pCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses_set', to='course.Category', verbose_name='课程种类')),
            ],
        ),
    ]
