# Generated by Django 3.2.6 on 2021-09-05 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_remove_orders_items_json'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='item_json',
            field=models.CharField(default='', max_length=5000),
        ),
    ]