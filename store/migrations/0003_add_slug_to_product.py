# Generated by Django 5.0.1 on 2024-02-21 06:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0002_rename_price_product_unit_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="slug",
            field=models.SlugField(default="-"),
            preserve_default=False,
        ),
    ]