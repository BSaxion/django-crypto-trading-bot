# Generated by Django 3.0.5 on 2020-05-08 14:11

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "exchange",
                    models.CharField(choices=[("binance", "Binance")], max_length=250),
                ),
                ("api_key", models.CharField(max_length=250)),
                ("secret", models.CharField(max_length=250)),
                ("password", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Bot",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("day_span", models.IntegerField(default=30)),
                (
                    "min_profit",
                    models.DecimalField(decimal_places=2, default=0.1, max_digits=30),
                ),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="trading_bot.Account",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Currency",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=50, null=True)),
                ("short", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Market",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("active", models.BooleanField(default=True)),
                (
                    "exchange",
                    models.CharField(choices=[("binance", "Binance")], max_length=250),
                ),
                ("precision_amount", models.IntegerField()),
                ("precision_price", models.IntegerField()),
                (
                    "limits_amount_min",
                    models.DecimalField(decimal_places=8, max_digits=30),
                ),
                (
                    "limits_amount_max",
                    models.DecimalField(decimal_places=8, max_digits=30),
                ),
                (
                    "limits_price_min",
                    models.DecimalField(decimal_places=8, max_digits=30),
                ),
                (
                    "limits_price_max",
                    models.DecimalField(decimal_places=8, max_digits=30),
                ),
                (
                    "base",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="base",
                        to="trading_bot.Currency",
                    ),
                ),
                (
                    "quote",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="quote",
                        to="trading_bot.Currency",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order_id", models.CharField(max_length=255, unique=True)),
                ("timestamp", models.DateTimeField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("open", "Open"),
                            ("closed", "Closed"),
                            ("canceled", "Canceled"),
                            ("expired", "Expired"),
                            ("rejected", "Rejected"),
                            ("reorderd", "Reorderd"),
                        ],
                        default="open",
                        max_length=10,
                    ),
                ),
                (
                    "exchange",
                    models.CharField(choices=[("binance", "Binance")], max_length=250),
                ),
                (
                    "order_type",
                    models.CharField(
                        choices=[("market", "Market"), ("limit", "Limit")], max_length=8
                    ),
                ),
                (
                    "side",
                    models.CharField(
                        choices=[("buy", "Side Buy"), ("sell", "Side Sell")],
                        max_length=4,
                    ),
                ),
                ("price", models.DecimalField(decimal_places=8, max_digits=30)),
                ("amount", models.DecimalField(decimal_places=8, max_digits=30)),
                (
                    "filled",
                    models.DecimalField(decimal_places=8, default=0, max_digits=30),
                ),
                ("fee_cost", models.DecimalField(decimal_places=8, max_digits=30)),
                (
                    "fee_rate",
                    models.DecimalField(
                        blank=True, decimal_places=8, max_digits=30, null=True
                    ),
                ),
                (
                    "bot",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="trading_bot.Bot",
                    ),
                ),
                (
                    "fee_currency",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="trading_bot.Currency",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Trade",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("trade_id", models.CharField(max_length=255, unique=True)),
                ("timestamp", models.DateTimeField()),
                (
                    "taker_or_maker",
                    models.CharField(
                        choices=[("market", "Market"), ("limit", "Limit")], max_length=8
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=8, max_digits=30)),
                ("fee_cost", models.DecimalField(decimal_places=8, max_digits=30)),
                (
                    "fee_rate",
                    models.DecimalField(
                        blank=True, decimal_places=8, max_digits=30, null=True
                    ),
                ),
                (
                    "fee_currency",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="trading_bot.Currency",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="trading_bot.Order",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Simulation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("day_span", models.IntegerField(default=30)),
                (
                    "min_profit",
                    models.DecimalField(
                        decimal_places=2,
                        default=Decimal(
                            "0.1000000000000000055511151231257827021181583404541015625"
                        ),
                        max_digits=30,
                    ),
                ),
                ("history_days", models.IntegerField(default=365)),
                ("start_simulation", models.DateTimeField()),
                ("end_simulation", models.DateTimeField()),
                ("simulation_amount", models.IntegerField()),
                (
                    "start_amount_eur",
                    models.DecimalField(decimal_places=8, max_digits=30),
                ),
                (
                    "end_amount_eur_average",
                    models.DecimalField(decimal_places=8, max_digits=30),
                ),
                ("roi_min", models.DecimalField(decimal_places=8, max_digits=30)),
                ("roi_average", models.DecimalField(decimal_places=8, max_digits=30)),
                ("roi_max", models.DecimalField(decimal_places=8, max_digits=30)),
                (
                    "market",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="trading_bot.Market",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OHLCV",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "timeframe",
                    models.CharField(
                        choices=[
                            ("1m", "Minute 1"),
                            ("3m", "Minute 3"),
                            ("5m", "Minute 5"),
                            ("15m", "Minute 15"),
                            ("30m", "Minute 30"),
                            ("1h", "Hour 1"),
                            ("2h", "Hour 2"),
                            ("4h", "Hour 4"),
                            ("6h", "Hour 6"),
                            ("8h", "Hour 8"),
                            ("12h", "Hour 12"),
                            ("1d", "Day 1"),
                            ("3d", "Day 3"),
                            ("1w", "Week 1"),
                            ("1M", "Month 1"),
                        ],
                        max_length=10,
                    ),
                ),
                ("timestamp", models.DateTimeField()),
                ("open_price", models.DecimalField(decimal_places=8, max_digits=30)),
                ("highest_price", models.DecimalField(decimal_places=8, max_digits=30)),
                ("lowest_price", models.DecimalField(decimal_places=8, max_digits=30)),
                ("closing_price", models.DecimalField(decimal_places=8, max_digits=30)),
                ("volume", models.DecimalField(decimal_places=8, max_digits=30)),
                (
                    "market",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="trading_bot.Market",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="bot",
            name="market",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="trading_bot.Market"
            ),
        ),
    ]
