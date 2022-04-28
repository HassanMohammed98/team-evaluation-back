from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Semester(models.Model):
    semester = models.CharField(max_length=30)
    year = models.PositiveIntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="semester")
    
    def __str__(self):
        return "Semester: %s %s" % (self.semester, str(self.year))
        
