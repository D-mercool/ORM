# Generated by Django 3.2.9 on 2021-11-15 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawyer', '0002_auto_20211116_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='type',
            field=models.CharField(max_length=255, verbose_name='Услуга'),
        ),
    ]
