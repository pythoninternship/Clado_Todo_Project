from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date=models.DateField()

    def __str__(self):
        return self.title



