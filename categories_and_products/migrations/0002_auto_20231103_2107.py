# Generated by Django 2.2.28 on 2023-11-03 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories_and_products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Restaurant',
            new_name='Vendor',
        ),
        migrations.AlterModelOptions(
            name='vendor',
            options={'verbose_name_plural': 'Vendors'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='Restaurant',
            new_name='Vendor',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Restaurant',
            new_name='Vendor',
        ),
        migrations.RenameField(
            model_name='vendor',
            old_name='restaurant_slug',
            new_name='vendor_slug',
        ),
    ]
