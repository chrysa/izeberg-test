from django.db import models


class TypeGroup(models.Model):
    type_name = models.CharField(max_length=30)
    type_id = models.IntegerField()

    def __str__(self):
        return self.type_name
