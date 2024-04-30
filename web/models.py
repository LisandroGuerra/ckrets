import uuid
from django.db import models


class System(models.Model):
    id = models.UUIDField(primary_key = True,
                          default = uuid.uuid4,
                          editable = False,
                          unique=True)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    acronym = models.CharField(max_length=10, unique=True, blank=False, null=False)
    contact_email = models.EmailField(max_length=100, blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Variable(models.Model):
    id = models.UUIDField(primary_key = True,
                          default = uuid.uuid4,
                          editable = False,
                          unique=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    value = models.CharField(max_length=256, blank=False, null=False)
    system = models.ForeignKey(System, on_delete=models.CASCADE, related_name='variables')

    class Meta:
        unique_together = ('name', 'system')

    def __str__(self):
        return self.name


# from django.core.management.utils import get_random_secret_key
# token = models.CharField(max_length=200, default=get_random_secret_key)
