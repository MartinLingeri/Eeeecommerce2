# Generated by Django 4.1.7 on 2023-03-22 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0005_alter_cartproduct_idcart_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('idpurchase', models.AutoField(db_column='idpurchase', primary_key=True, serialize=False)),
                ('user', models.IntegerField(db_column='users_idusers')),
                ('date', models.DateTimeField(db_column='date')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseProduct',
            fields=[
                ('idpurchase_product', models.AutoField(db_column='idpurchase_product', primary_key=True, serialize=False)),
                ('purchase', models.IntegerField(db_column='purchase_idpurchase')),
                ('product', models.IntegerField(db_column='product_idproduct')),
                ('quantity', models.IntegerField(db_column='quantity')),
                ('price', models.FloatField(db_column='price')),
            ],
        ),
    ]
