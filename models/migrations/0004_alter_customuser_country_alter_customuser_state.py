# Generated by Django 4.1.7 on 2023-03-09 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_alter_cart_user_alter_cartproduct_cart_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='country',
            field=models.IntegerField(default=1010),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='state',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
