# Generated by Django 5.0.7 on 2024-08-08 07:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0002_alter_course_preview_alter_lesson_link_and_more"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
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
                ("date", models.DateTimeField(auto_now_add=True, verbose_name="Дата")),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "type_of_payment",
                    models.CharField(
                        choices=[("Cash", "наличные"), ("Transfer", "перевод ")],
                        verbose_name="Способ Оплаты",
                    ),
                ),
                (
                    "payed_course",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="materials.course",
                        verbose_name="Оплаченный курс",
                    ),
                ),
                (
                    "payed_lesson",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="materials.lesson",
                        verbose_name="Оплаченный урок",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Платеж",
                "verbose_name_plural": "Платежи",
                "ordering": ["-date"],
            },
        ),
    ]
