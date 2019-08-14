from django.db import models
from user.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()
    description = models.CharField(max_length = 500)
    quantity = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True, blank=True)
    
class Auction(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    number_of_bids = models.IntegerField()
    time_starting = models.DateTimeField()
    time_ending = models.DateTimeField()
    
class Watchlist(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
    
class Bid(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
    bid_time = models.DateTimeField()
    
class Chat(models.Model):
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    time_sent = models.DateTimeField()