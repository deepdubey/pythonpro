# Generated by Django 2.0.2 on 2018-03-17 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_remove_cart_pr_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='pr_logo',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
    ]
