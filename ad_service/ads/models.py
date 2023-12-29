from django.db import models

class Location(models.Model):
    location_name = models.CharField(max_length=255)

    def __str__(self):
        return self.location_name

class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

class User(models.Model):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    passphrase = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    user_status = models.IntegerField()
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

class Ad(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    createdAd = models.DateTimeField(auto_now_add=True)
    updatedAd = models.DateTimeField(auto_now=True)
    visibility = models.CharField(max_length=10, choices=[('public', 'Public'), ('local', 'Local')], default='public')

    def __str__(self):
        return self.title
