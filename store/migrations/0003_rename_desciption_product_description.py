# Generated by Django 4.1 on 2022-08-29 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='desciption',
            new_name='description',
        ),
    ]