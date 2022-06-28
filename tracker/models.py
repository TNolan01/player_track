from django.db import models
from datetime import timedelta, date
from django.urls import reverse
from django.utils import timezone
import datetime


class Player(models.Model):
    name = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=200, null=True)
    irish_name = models.CharField(max_length=200, null=True, default='to be confirmed')
    date_of_birth = models.DateField(null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
    
    @property
    def Age(self):
        today = datetime.date.today()
        age = (today - self.date_of_birth)
        age_days = str(age).split("d",1)[0]
        age_formatted = round((int(age_days)/365),1)
        return age_formatted
    
 
class Session(models.Model):
    session_name = models.CharField(max_length=200, null=True)
    session_date = models.DateField(null=True)    
    player = models.ManyToManyField(Player)
   

    def __str__(self):
        return str(self.session_date)
    
    class Meta:
        ordering = ('session_date',)
    
    
class Match(models.Model):
    VENUE = [
        ('Home', 'Home'),
        ('Away', 'Away')
        ]
    
    match_date = models.DateField(null=True)
    match_details = models.CharField(max_length=200, null=True)
    venue = models.CharField(max_length=5, choices=VENUE, unique=False)
    
    
    def __str__(self):
        return str(self.match_date)
    
    class Meta:
        ordering = ('match_date',)
    

class Team_Selection(models.Model):
    STATUS = [
        ('Starting', 'Starting'),
        ('Sub', 'Sub')
        ]
    JERSEY = [(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,12),(13,13),(14,14),(15,15),(16,16),(17,17),(18,18),(19,19),(20,20),(21,21),(22,22),(23,23),(24,24),(25,25)]
          
    match = models.ForeignKey(Match, on_delete=models.CASCADE, null=True)
    player = models.ManyToManyField(Player, blank=True)
    jersey_number = models.IntegerField(choices=JERSEY, null=True, blank=True)
    game_status = models.CharField(max_length=10, choices=STATUS, blank=True)
    goals = models.IntegerField(null=True, blank=True)
    points = models.IntegerField(null=True, blank=True)
    notes  = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.match)



class Club(models.Model):
    club_name = models.CharField(max_length=200, null=True, default='Club Name')
    
    def __str__(self):
        return self.club_name
  