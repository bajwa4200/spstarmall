# Generated by Django 2.2.4 on 2024-04-17 17:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_item_discount_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='pack_size',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='por',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='price_inc_vat',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='rrp',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='vat',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]