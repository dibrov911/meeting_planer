from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=50)
    floor = models.IntegerField()
    room_number = IntegerField()
    def __str__(self):
         return f"{self.name}: room {self.room_number} on floor {self.floor}"

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=9)
    duration =  models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    def __str__(self):
        return f" Meeting: {self.title} start time on {self.date}"

