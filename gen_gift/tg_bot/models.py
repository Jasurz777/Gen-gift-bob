from django.utils.text import slugify
from django.db import models


class Log(models.Model):
    user_id = models.BigIntegerField()
    messages = models.JSONField(default={'state': 0})


class User(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=128, null=True)
    name = models.CharField(max_length=128, null=True)
    phone = models.CharField(max_length=15, null=True)
    lang = models.IntegerField(null=True, default=1)
    menu = models.IntegerField(null=True, default=0)

    def __str__(self):
        return f"{self.user_id} {self.username}"


class Category(models.Model):
    name_uz = models.CharField(max_length=128, null=True)
    name_ru = models.CharField(max_length=128, null=True)

    def __str__(self):
        return f"{self.name_uz}"


class Human(models.Model):
    name_uz = models.CharField(max_length=128)
    name_ru = models.CharField(max_length=128)
    ctg = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name_uz


class Situation(models.Model):
    name_uz = models.CharField(max_length=128)
    name_ru = models.CharField(max_length=128)
    human = models.ManyToManyField(Human)

    def __str__(self):
        return self.name_uz


class Interests(models.Model):
    name_uz = models.CharField(max_length=128, null=True)
    name_ru = models.CharField(max_length=128, null=True)
    situation = models.ManyToManyField(Situation)

    def __str__(self):
        return f"{self.name_uz}"


class Cash(models.Model):
    name_uz = models.CharField(max_length=128, null=True)
    name_ru = models.CharField(max_length=128, null=True)
    interests = models.ManyToManyField(Interests)

    def __str__(self):
        return f"{self.name_uz}"


class Agee(models.Model):
    name_uz = models.CharField(max_length=128, null=True)
    name_ru = models.CharField(max_length=128, null=True)
    cash = models.ManyToManyField(Cash)

    def __str__(self):
        return f"{self.name_uz}"


class Product(models.Model):
    name_uz = models.CharField(max_length=128, null=True, blank=True)
    name_ru = models.CharField(max_length=128, null=True, blank=True)
    img = models.ImageField()
    description_uz = models.TextField(null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    age = models.ManyToManyField(Agee)
    price = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return f"{self.name_uz}"


class Savat(models.Model):
    user_id = models.BigIntegerField()
    slug = models.SlugField(max_length=128, null=True)
    product = models.CharField(max_length=256)
    amount = models.IntegerField(null=True)
    priceproduct = models.CharField(max_length=128, null=True)
    summ = models.IntegerField(null=True)
    til = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product)

        return super(Savat, self).save(*args, **kwargs)

    def __str__(self):
        return self.product
