# Generated by Django 2.2.28 on 2023-11-03 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(max_length=250, unique=True)),
                ('display_name', models.CharField(blank=True, max_length=250, null=True)),
                ('categoryslug', models.SlugField(blank=True, null=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Categories')),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=250, null=True, unique=True)),
                ('restaurant_slug', models.SlugField(unique=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('Longitude', models.FloatField(blank=True, default=0, null=True)),
                ('Latitude', models.FloatField(blank=True, default=0, null=True)),
                ('delivery_fees', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Restaurants',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('ArabicName', models.CharField(blank=True, max_length=250, null=True)),
                ('productslug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.FloatField(default=0)),
                ('boughtPrice', models.FloatField(blank=True, default=0, null=True)),
                ('offerPercentage', models.FloatField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('Most_Popular', models.BooleanField(default=False)),
                ('New_Products', models.BooleanField(default=False)),
                ('Best_Offer', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('limit', models.IntegerField(blank=True, default=0, null=True)),
                ('Restaurant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories_and_products.Restaurant')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories_and_products.Category')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='Restaurant',
            field=models.ManyToManyField(blank=True, to='categories_and_products.Restaurant'),
        ),
    ]
