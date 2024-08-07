# Generated by Django 2.2.4 on 2024-07-03 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20240426_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_pickup',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='core.Subcategory'),
        ),
    ]
