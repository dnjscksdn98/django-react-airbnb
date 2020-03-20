from django.db import models


class TimeStampedModel(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # when it is used as a base class for other models,
        # its fields will be added to those of the child class.
        abstract = True
