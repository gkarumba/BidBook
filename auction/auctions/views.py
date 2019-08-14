from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import permissions
from rest_framework import viewsets, mixins, generics
# Create your views here.

class CategoryView(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Category.object.all()
    serializer_class = CategorySerializer
    
class ProductView(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class AuctionView(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Auction.objects.all()
    serializer_class = AuctionSerialiser
    
class WatchlistView(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer
    
class BidView(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    
class ChatView(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer