from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Semester(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    semester = models.CharField(max_length=30)
    year = models.PositiveIntegerField()
    
    def __str__(self):
        return "Semester: %s %s" % (self.semester, str(self.year))
        
