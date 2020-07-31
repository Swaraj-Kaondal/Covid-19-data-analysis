from django.db import models
from django.contrib.postgres.fields import ArrayField

class CARDdata(models.Model):
	Data_ID = models.IntegerField(primary_key = True)
	Confirmed = models.IntegerField()
	Active =  models.IntegerField()
	Recovered =  models.IntegerField()
	Deceased =  models.IntegerField()

class Tweet(models.Model):
	TweetId = models.BigIntegerField(primary_key=True)
	Sentiment = models.FloatField()

class Patient(models.Model):
	Id = models.IntegerField(primary_key=True)
	Age = models.IntegerField()
	Name = models.CharField(max_length = 100)
	Gender = models.CharField(max_length = 10)
	Status = models.CharField(max_length = 100)

class DateAndArea(models.Model):
	Id = models.IntegerField(primary_key=True)
	State = models.CharField(max_length=50)
	Date = models.DateField()

class Tweets(models.Model):
	TweetId = models.BigIntegerField(primary_key=True)
	DateAndAreaId = models.IntegerField()

class Status(models.Model):
	CARDdataId = models.IntegerField(primary_key=True)
	DateAndAreaId = models.IntegerField()

class From(models.Model):
	PatientId = models.IntegerField(primary_key=True)
	DateAndAreaId = models.IntegerField()