from django.db import models

# Create your models here.

class TestModel(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True, blank=True )
    description = models.TextField()
    phone_number = models.PositiveIntegerField()
    is_live = models.BooleanField()
    amount = models.FloatField()
# name = models.TextField(error_messages={"null":"this field cannot be null",
#     "blank":"this field cannot be null"})
# name = models.IntegerField()
# name = models.BigIntegerField()
# name = models.PositiveIntegerField()
# name = models.FloatField()
# name = models.BooleanField()
# name = models.ManyToManyField()
# name = models.OneToOneField()
# name = models.ForeignKey()