# Generated by Django 4.0 on 2021-12-12 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Book',
        ),
    ]
