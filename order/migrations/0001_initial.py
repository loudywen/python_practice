# Generated by Django 2.1 on 2018-09-25 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=250)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='USD Order Total')),
                ('emailAddress', models.EmailField(blank=True, max_length=250, verbose_name='Email Address')),
                ('created', models.DateField(auto_now_add=True)),
                ('billingName', models.CharField(blank=True, max_length=250)),
                ('billingAddress1', models.CharField(blank=True, max_length=250)),
                ('billingCity', models.CharField(blank=True, max_length=250)),
                ('billingPostcode', models.CharField(blank=True, max_length=10)),
                ('billingCountry', models.CharField(blank=True, max_length=250)),
                ('shippingName', models.CharField(blank=True, max_length=250)),
                ('shippingAddress1', models.CharField(blank=True, max_length=250)),
                ('shippingCity', models.CharField(blank=True, max_length=250)),
                ('shippingPostcode', models.CharField(blank=True, max_length=10)),
                ('shippingCountry', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'db_table': 'Order',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='USD Price')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order')),
            ],
            options={
                'db_table': 'OrderItem',
            },
        ),
    ]
