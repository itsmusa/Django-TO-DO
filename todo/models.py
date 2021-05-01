from django.db import models


class Task(models.Model):
    details = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    class Meta:
        ordering = ['time_created',]

    def __str__(self):
        return self.details
