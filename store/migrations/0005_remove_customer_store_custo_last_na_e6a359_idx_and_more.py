# Generated by Django 5.0.1 on 2024-02-21 06:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0004_customer_store_custo_last_na_e6a359_idx_and_more"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="customer",
            name="store_custo_last_na_e6a359_idx",
        ),
        migrations.AlterModelTable(
            name="customer",
            table=None,
        ),
    ]
