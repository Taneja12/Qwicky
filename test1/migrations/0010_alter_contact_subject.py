# Generated by Django 4.2.4 on 2023-10-03 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0009_remove_contact_name_contact_subject_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=50),
        ),
    ]