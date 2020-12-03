# Generated by Django 2.0 on 2018-12-05 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20181204_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='configure',
            field=models.CharField(default='', max_length=200, verbose_name='配置'),
        ),
        migrations.AddField(
            model_name='question',
            name='number',
            field=models.CharField(default='', max_length=50, verbose_name='编号'),
        ),
        migrations.AddField(
            model_name='question',
            name='permanent_asset_number',
            field=models.CharField(default='', max_length=50, verbose_name='固定资产编号'),
        ),
        migrations.AddField(
            model_name='question',
            name='price',
            field=models.IntegerField(default=0, verbose_name='金额'),
        ),
        migrations.AddField(
            model_name='question',
            name='product_factory',
            field=models.CharField(default='', max_length=200, verbose_name='生产厂家'),
        ),
        migrations.AddField(
            model_name='question',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='数量'),
        ),
        migrations.AddField(
            model_name='question',
            name='relate_project',
            field=models.CharField(default='', max_length=50, verbose_name='关联项目'),
        ),
        migrations.AddField(
            model_name='question',
            name='remark',
            field=models.CharField(default='', max_length=200, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='question',
            name='mobile_brand',
            field=models.CharField(max_length=200, verbose_name='资产名称'),
        ),
        migrations.AlterField(
            model_name='question',
            name='mobile_model',
            field=models.CharField(max_length=200, verbose_name='规格型号'),
        ),
    ]