# Generated by Django 4.2.4 on 2023-08-24 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Description',
            field=models.CharField(max_length=500),
        ),
    ]