from django.db import models

# Create your models here.
class State(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name
class City(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    state_id=models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        related_name='cities'
    )
    def __str__(self):
        return self.name
class Profile(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    mobile=models.CharField(max_length=10)
    street_adrs=models.CharField(max_length=255)
    state=models.ForeignKey(
        State,
        on_delete=models.CASCADE
    )
    city=models.ForeignKey(
        City,
        on_delete=models.CASCADE
    )
    pincode=models.IntegerField()
