from django.db import models

# Create your models here.
class ticket(models.Model):
    ticketFor = models.CharField(max_length=100, null=False)
    date = models.DateField()
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    status = models.IntegerField()
    name = models.CharField(max_length=100)
    contact = models.IntegerField()
    file = models.FileField()
    noteByAuthority = models.CharField(max_length=200,null=False,default=None)

