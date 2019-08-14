from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('categories',views.CategoryView)
router.register('products',views.ProductView)
router.register('auctions', views.AuctionView)
router.register('watchlists',views.WatchlistView)
router.register('bids',views.BidView)
router.register('chats',views.ChatView)

urlpatterns = [
    path('', include(router.urls)),
    path('auth-login', include('rest_framework.urls'))
]