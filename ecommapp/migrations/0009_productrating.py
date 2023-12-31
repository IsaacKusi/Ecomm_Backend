# Generated by Django 4.2.2 on 2023-07-14 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("ecommapp", "0008_customeraddress_default_address"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductRating",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rating", models.IntegerField()),
                ("review", models.TextField()),
                ("date_time", models.DateTimeField(auto_now_add=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="customer_ratings",
                        to="ecommapp.customer",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_rating",
                        to="ecommapp.product",
                    ),
                ),
            ],
        ),
    ]
