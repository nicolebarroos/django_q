from django.db import models


class TaskMessage(models.Model):
    message = models.CharField(max_length=150)

    def __str__(self):
        return self.message

