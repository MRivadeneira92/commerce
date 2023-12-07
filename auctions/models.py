from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    active_listing = models.ManyToManyField("Listing")
    user_comments = models.ManyToManyField("Comments")

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=200)
    starting_bid = models.IntegerField()
    image = models.URLField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ManyToManyField("Comments")
    categories = models.ForeignKey("Categories",null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.title}: {self.starting_bid}"

class Comments(models.Model):
    author = models.ForeignKey("User", on_delete=models.CASCADE)
    comment = models.TextField()
    com_listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="com_listing")

class Categories(models.Model):
    category = ("used", "new")
    cat_listing = models.ManyToManyField(Listing, related_name="cat_listing")