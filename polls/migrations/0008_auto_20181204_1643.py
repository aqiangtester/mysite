# Generated by Django 2.0 on 2018-12-04 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20181204_1522'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['pub_date'], 'verbose_name': '测试手机', 'verbose_name_plural': '测试手机'},
        ),
        migrations.AlterField(
            model_name='question',
            name='mobile_model',
            field=models.CharField(max_length=200, verbose_name='型号'),
        ),
    ]
