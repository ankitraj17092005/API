from django.db import models

# Create your models here.
class Branch(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Student(models.Model):
    gender_c=[('Male','Male'),('Female','Female'),('other','other')]
    
    name=models.CharField(max_length=255)
    gender=models.CharField(choices=gender_c)
    roll=models.IntegerField()
    branch=models.ForeignKey(
        Branch,
        
        on_delete=models.CASCADE
    )
    summary=models.TextField()
