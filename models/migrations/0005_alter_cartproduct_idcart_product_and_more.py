# Generated by Django 4.1.7 on 2023-03-15 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0004_alter_customuser_country_alter_customuser_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='idcart_product',
            field=models.AutoField(db_column='idcart_product', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='idcategory',
            field=models.AutoField(db_column='idcategory', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='idproduct',
            field=models.AutoField(db_column='idproduct', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='idproduct_image',
            field=models.AutoField(db_column='idproduct_image', primary_key=True, serialize=False),
        ),
    ]
