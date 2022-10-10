from django.db import models


class Ticket(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.text

