# Generated by Django 4.1.1 on 2023-06-15 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_category_created_at_category_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(upload_to='categories/'),
        ),
    ]