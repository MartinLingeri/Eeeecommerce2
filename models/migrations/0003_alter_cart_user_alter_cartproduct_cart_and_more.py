# Generated by Django 4.1.7 on 2023-03-09 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.IntegerField(db_column='users_idusers'),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='cart',
            field=models.IntegerField(db_column='cart_idcart'),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='product',
            field=models.IntegerField(db_column='product_idproduct'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.IntegerField(db_column='category_idcategory'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.IntegerField(db_column='product_idproduct'),
        ),
        migrations.AlterField(
            model_name='state',
            name='country',
            field=models.IntegerField(db_column='countries_idcountries'),
        ),
    ]