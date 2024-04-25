from django.db import models

# Create your models here.
class Event(models.Model):
    image=models.ImageField(upload_to="pic")
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    location=models.CharField(max_length=100)
    event_date=models.DateField()
    def __str__(self):
        return self.name

class Registration(models.Model):
    reg_name=models.CharField(max_length=50)
    reg_email=models.CharField(max_length=50)
    name=models.ForeignKey(Event, on_delete=models.CASCADE)
    reg_date=models.DateField(auto_now=True)
    # def __str__(self):
    #     return self.name