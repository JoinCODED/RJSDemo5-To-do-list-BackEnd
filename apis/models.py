from django.db import models

# Create your models here.
class Task(models.Model):
	HIGH = 'high'
	MIDDLE = 'middle'
	LOW = 'low'
	PRIORITY_CHOICES = (
		(HIGH, 'high'),
		(MIDDLE, 'middle'),
		(LOW, 'low'),
	)
	task = models.CharField(max_length=250)
	done = models.BooleanField()
	priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default=LOW)


 