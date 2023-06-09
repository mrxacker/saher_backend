# Generated by Django 4.1.1 on 2023-06-11 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subcategories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='products/')),
                ('price_old', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('price_new', models.DecimalField(decimal_places=2, max_digits=8)),
                ('desc', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='subcategories.subcategory')),
            ],
        ),
    ]
