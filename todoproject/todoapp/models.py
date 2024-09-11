from unicodedata import category
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300, blank=True, null=True)
    category = models.ForeignKey("Category", null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey("Status", on_delete=models.PROTECT)
    till_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Status(models.Model):
    title = models.CharField(max_length=100)
    is_default = models.BooleanField()

    def __str__(self):
        return self.title