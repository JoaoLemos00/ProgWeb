# Generated by Django 4.2.5 on 2023-09-20 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='doby',
            new_name='body',
        ),
    ]
