# Generated by Django 4.2.4 on 2023-10-03 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0008_remove_contact_subject_contact_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default='Unknown', max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=30),
        ),
    ]
