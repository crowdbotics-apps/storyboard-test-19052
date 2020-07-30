from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Store(models.Model):
    "Generated Model"
    name = models.CharField(max_length=256,)
    email = models.EmailField(max_length=254,)
    phone = models.CharField(max_length=256,)
    location = models.ForeignKey(
        "home.Location", on_delete=models.CASCADE, related_name="store_location",
    )
    category = models.ForeignKey(
        "home.Category", on_delete=models.CASCADE, related_name="store_category",
    )


class Location(models.Model):
    "Generated Model"
    name = models.CharField(max_length=256,)
    address = models.CharField(max_length=256,)
    city = models.CharField(max_length=256,)
    state = models.CharField(max_length=2,)
    zip = models.CharField(max_length=5,)


class Category(models.Model):
    "Generated Model"
    equipment = models.CharField(max_length=256,)
    coaching = models.CharField(max_length=256,)
    teams = models.CharField(max_length=256,)
