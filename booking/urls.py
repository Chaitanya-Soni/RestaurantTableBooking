from django.contrib import admin
from django.urls import path ,include
from .views import TableApi,BookingApi,BookingShedule,BookingView

#from .views import posts ,postsDetail
urlpatterns = [
    path('tables/', TableApi.as_view()),
    path('booking/<int:id>', BookingApi.as_view()),
    path('bookingShedule/', BookingShedule.as_view()),
    path('bookingDetail/<int:id>', BookingView.as_view()),
]