from django.db import models

# Create your models here.
class table(models.Model):
    name = models.CharField(max_length = 20)
    seats = models.IntegerField()

class BookingTime(models.Model):
    tablebook = models.ForeignKey(table, on_delete=models.CASCADE)
    stime = models.DateTimeField()
    etime = models.DateTimeField()
