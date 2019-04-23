from django.db import models

# Create your models here.


class JobsModel(models.Model):
	jobName = models.CharField(max_length=120, blank=True, null=True)
	jobDescription = models.TextField(max_length=120, blank=True, null=True)
	jobsLink = models.CharField(max_length=120, blank=True, null=True)

	def __str__(self):
		return self.jobName