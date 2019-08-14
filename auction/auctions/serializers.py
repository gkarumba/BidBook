from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)
        
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        field = ('title','image','description','quantity','category','date_posted')
        
class AuctionSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Auction
        fields = ('product_id','number_of_bids','time_starting','time_ending')
        
class Watchlist(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Watchlist
        fields = ('user_id','auction_id')
        
class BidSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bid
        fields = (' user_id','auction_id','bid_time')
    
class ChatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chat
        fields = ('auction_id','user_id','message','time_sent')       