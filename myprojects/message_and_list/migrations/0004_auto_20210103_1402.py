# Generated by Django 3.1 on 2021-01-03 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_and_list', '0003_auto_20210103_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='feuture',
            field=models.BooleanField(default=False),
        ),
    ]
