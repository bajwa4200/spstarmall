# Generated by Django 2.2.4 on 2024-07-04 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20240703_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='core.Subcategory'),
        ),
    ]
