# Generated by Django 3.2 on 2021-05-07 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=120)),
                ('price', models.IntegerField()),
                ('spec', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
