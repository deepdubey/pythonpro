# Generated by Django 2.0.2 on 2018-03-16 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_pr_offer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['pr_id']},
        ),
    ]
