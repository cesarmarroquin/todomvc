from django.db import models


# Make these fields
# id
# title - string, required
# completed - boolean, default false
# order - integer, not required, can be null


class ToDo(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    order = models.IntegerField(blank=True, null=True)

