# Generated by Django 4.2.4 on 2023-10-01 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0004_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
    ]
