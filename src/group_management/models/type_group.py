from django.db import models


class TypeGroup(models.Model):
    type_name = models.CharField(max_length=30)

    def __str__(self):
        return self.type_name
