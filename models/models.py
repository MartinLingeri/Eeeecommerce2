from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.utils.translation import gettext as _


class Countries(models.Model):
    idcountries = models.IntegerField(
        db_column='idcountries', primary_key=True)
    name = models.CharField(db_column='name', max_length=255)
    ccode = models.CharField(db_column='ccode', unique=True, max_length=2)

    class Meta:
        managed = True


class State(models.Model):
    idstate = models.IntegerField(db_column='idstate', primary_key=True)
    name = models.CharField(db_column='name', max_length=255)
    country = models.IntegerField(db_column='countries_idcountries')


class Category(models.Model):
    idcategory = models.AutoField(db_column='idcategory', primary_key=True)
    name = models.CharField(db_column='name', unique=True, max_length=45)


class Product(models.Model):
    idproduct = models.AutoField(db_column='idproduct', primary_key=True)
    name = models.CharField(db_column='name', max_length=45)
    description = models.CharField(db_column='description', max_length=255)
    price = models.FloatField(db_column='price')
    category = models.IntegerField(db_column='category_idcategory')


class ProductImage(models.Model):
    idproduct_image = models.AutoField(
        db_column='idproduct_image', primary_key=True)
    image = models.CharField(db_column='image', max_length=255)
    product = models.IntegerField(db_column='product_idproduct')


class CustomUserManager(BaseUserManager):
    def create_user(self, nombre, contrasenia, country=1010, state=230):
        if not nombre:
            raise ValueError('Users must have an username')
        if not state:
            raise ValueError('Users must have a state')
        user = self.model(
            nombre=nombre,
            state=state,
            country=country
        )
        user.set_password(contrasenia)
        user.save(using=self._db)
        return user

    def create_superuser(self, nombre, contrasenia):
        user = self.create_user(
            nombre=nombre,
            contrasenia=contrasenia,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=45, unique=True)
    contrasenia = models.CharField(max_length=45)
    state = models.IntegerField(null=True, default=None)
    country = models.IntegerField(default=1010)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to.'),
        related_name='custom_users'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='custom_users_permissions'
    )

    USERNAME_FIELD = "nombre"
    REQUIRED_FIELDS = ["contrasenia", "state"]

    def __str__(self):
        return self.nombre


class Cart(models.Model):
    idcart = models.IntegerField(db_column='idcart', primary_key=True)
    user = models.IntegerField(db_column='users_idusers')


class CartProduct(models.Model):
    idcart_product = models.AutoField(
        db_column='idcart_product', primary_key=True)
    cart = models.IntegerField(db_column='cart_idcart')
    product = models.IntegerField(db_column='product_idproduct')
    quantity = models.IntegerField(db_column='quantity')

class Purchase(models.Model):
    idpurchase = models.AutoField(
        db_column='idpurchase', primary_key=True)
    user = models.IntegerField(db_column='users_idusers')
    date = models.DateTimeField(db_column='date')

class PurchaseProduct(models.Model):
    idpurchase_product = models.AutoField(
        db_column='idpurchase_product', primary_key=True)
    purchase = models.IntegerField(db_column='purchase_idpurchase')
    product = models.IntegerField(db_column='product_idproduct')
    quantity = models.IntegerField(db_column='quantity')
    price = models.FloatField(db_column='price')

class Payments(models.Model):
    idpayments = models.AutoField(
        db_column='idpayments', primary_key=True)
    purchase = models.IntegerField(db_column='purchase_idpurchase')
    date = models.DateTimeField(db_column='date')
    amount = models.FloatField(db_column='amount')
    status = models.CharField(db_column='status', max_length=45)