from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=60)
    price = models.FloatField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    published_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
