from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from semesters.models import Semester


# Create your models here.
class Project(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    weight = models.IntegerField(
        default=100,
        validators=[MaxValueValidator(100), MinValueValidator(1)]
    )

    
    def __str__(self):
        return "Project: %s (%s percent) -%s %s" % (self.name, str(self.weight), self.semester.semester, self.semester.year)