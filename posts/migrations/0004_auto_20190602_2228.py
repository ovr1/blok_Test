# Generated by Django 2.1.5 on 2019-06-02 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20190602_1655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='slug',
            new_name='cat_slug',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='cat_title',
        ),
    ]
