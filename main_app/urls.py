from django.urls import path
from .views import Home, DogList, DogDetail
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('Dogs/',DogList.as_view(), name='dog-list'),
    path('Dogs/<int:id>', DogDetail.as_view(), name='dog-detail'),
]