from rest_framework import serializers
from .models import table,BookingTime
class tableSerializer (serializers.ModelSerializer):
    class Meta :
        model = table
        fields = ["id","name","seats"]
class BookingTimeSerializer (serializers.ModelSerializer):
    class Meta :
        model = BookingTime
        fields = ["id","stime","etime"]