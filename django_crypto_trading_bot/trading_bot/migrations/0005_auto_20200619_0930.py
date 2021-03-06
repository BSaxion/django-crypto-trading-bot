# Generated by Django 3.0.5 on 2020-06-19 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trading_bot", "0004_auto_20200618_1727"),
    ]

    operations = [
        migrations.RemoveField(model_name="bot", name="day_span",),
        migrations.RemoveField(model_name="bot", name="min_profit",),
        migrations.AddField(
            model_name="bot",
            name="timeframe",
            field=models.CharField(
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
                default="1M",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("open", "Open"),
                    ("closed", "Closed"),
                    ("canceled", "Canceled"),
                    ("expired", "Expired"),
                    ("rejected", "Rejected"),
                ],
                default="open",
                max_length=10,
            ),
        ),
        migrations.DeleteModel(name="Simulation",),
    ]
