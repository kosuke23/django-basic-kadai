# Generated by Django 4.2.11 on 2024-04-03 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crud", "0003_product_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="img",
            field=models.ImageField(blank=True, default="noImage.png", upload_to=""),
        ),
    ]
