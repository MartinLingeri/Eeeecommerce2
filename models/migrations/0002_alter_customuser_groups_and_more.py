# Generated by Django 4.1.7 on 2023-03-09 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='custom_users', to='auth.group', verbose_name='grupos'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Permisos específicos para este usuario.', related_name='custom_users_permissions', to='auth.permission', verbose_name='permisos de usuario'),
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(db_column='name', max_length=255),
        ),
    ]
