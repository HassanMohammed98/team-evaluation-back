from django.db import models

# Create your models here.
class Semester(models.Model):
	semester = models.CharField(max_length=30)
	year = models.PositiveIntegerField()

	def __str__(self):
		return "Semester: %s %s" % (self.semester, str(self.year))