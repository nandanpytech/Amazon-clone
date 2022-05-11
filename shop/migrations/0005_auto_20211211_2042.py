# Generated by Django 3.2.3 on 2021-12-11 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_customer_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='info',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='product',
            name='model',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='product',
            name='specify',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='product',
            name='storage',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='prname',
            field=models.CharField(default='', max_length=200),
        ),
    ]
