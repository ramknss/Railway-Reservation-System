from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.
class User(AbstractUser):
	g = [
		('0','--- Select Your Gender ---'),
		('1','Male'),
		('2','Female'),
		('3','Other')
	]
	c = [
		('0','Admin'),
		('1','Customer'),
	]
	mble = models.CharField(max_length=10,null=True,blank=True)
	gdr = models.CharField(choices=g,default='0',max_length=5)
	pfimg = models.ImageField(upload_to='Profiles/',default='pfle.png')

class Train(models.Model):
    y = [
        ('s', 'Select your Train Type'),
        ('Passenger', 'Passenger'),
        ('Vande_Bharat', 'Vande_Bharat'),
        ('Express', 'Express'),
        ('Mail','Mail',)
    ]
    trainnum = models.CharField(max_length=10, null=True, blank=True)
    traintype = models.CharField(choices=y, default='s', max_length=15)
    trainsrc = models.CharField(max_length=30, null=True, blank=True)
    traindes = models.CharField(max_length=30, null=True, blank=True)
    deptimesrc = models.DateTimeField(null=True, blank=True)
    arrtimedes = models.DateTimeField(null=True, blank=True)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


class Rform(models.Model):
	usname = models.CharField(max_length=50,null=True,blank=True)
	name = models.CharField(max_length=50,null=True,blank=True)
	pno = models.CharField(max_length=10,null=True,blank=True)
	noft = models.IntegerField(null=True,blank=True)
	train = models.ForeignKey(Train, on_delete=models.CASCADE, null=True, blank=True)

class Story(models.Model):
    Title = models.TextField(max_length=20,null=True,blank=True)
    writername = models.CharField(max_length=100,null=True,blank=True)
    story = models.TextField(null=False)
    

