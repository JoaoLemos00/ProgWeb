# Generated by Django 4.2.4 on 2023-09-22 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blogpost_date_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='date updated'),
        ),
    ]
