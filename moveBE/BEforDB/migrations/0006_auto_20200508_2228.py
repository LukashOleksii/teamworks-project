# Generated by Django 2.2.6 on 2020-05-08 19:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BEforDB', '0005_auto_20200420_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='shoe',
        ),
        migrations.AddField(
            model_name='color',
            name='image',
            field=models.CharField(default='null', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='favorite',
            name='color',
            field=models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, to='BEforDB.Color'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderlist',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderlist',
            name='user',
            field=models.ForeignKey(blank=True, default='null', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoe',
            name='image',
            field=models.CharField(default='null', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='color',
            name='shoe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='color', to='BEforDB.Shoe'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 5, 8, 22, 27, 47, 647953)),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 5, 8, 22, 27, 47, 647953)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Not_Confirmed', 'Not confirmed'), ('Pacing', 'Pacing'), ('Delivered', 'Delivered'), ('Delivery', 'Delivery')], default='Not_Confirmed', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=14, region=None),
        ),
        migrations.AlterField(
            model_name='order',
            name='shoes',
            field=models.ManyToManyField(related_name='order', to='BEforDB.OrderList'),
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='size',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='size', to='BEforDB.Color'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
