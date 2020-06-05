from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=50, null=True)
    profile_pic = models.ImageField(default="default_profile.png", null=True, blank=True)
    mobile = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.username


class Category(models.Model):
    category = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.category


class Actor(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        name = self.first_name + ' ' + self.last_name
        return name


class Inventory(models.Model):
    inventory = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.inventory)


class Director(models.Model):
    director = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.director


class Movie(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.ManyToManyField(Category, blank=True)
    description = models.CharField(max_length=200, null=True)
    actor = models.ManyToManyField(Actor, blank=True)
    director = models.ForeignKey(Director, null=True, on_delete=models.CASCADE, blank=True)
    inventory = models.ForeignKey(Inventory, null=True, on_delete=models.CASCADE, blank=True)
    image = models.ImageField(default="store.png", null=True, blank=True)

    def __str__(self):
        return self.name



class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        ordered_movies = self.movieorder_set.all()
        for i in ordered_movies:
            shipping = True
        return shipping

    @property
    def get_cart_total(self):
        ordered_movies = self.movieorder_set.all()
        total = sum([movie.get_total for movie in ordered_movies])
        return total

    @property
    def get_cart_items(self):
        ordered_movies = self.movieorder_set.all()
        total = sum([movie.quantity for movie in ordered_movies])
        return total


class AddressCustomer(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    addres = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.addres


class MovieOrder(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    @property
    def get_total(self):
        total = self.movie.price * self.quantity
        return total


class City(models.Model):
    city = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.city


class Store(models.Model):
    address = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    profile_pic = models.ImageField(default="default_profile.png", null=True, blank=True)

    def __str__(self):
        return self.address
