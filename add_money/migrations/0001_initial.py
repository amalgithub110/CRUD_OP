# Generated by Django 5.2.3 on 2025-06-28 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add_money',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_what', models.CharField(max_length=255)),
                ('how_much', models.IntegerField()),
            ],
        ),
    ]
