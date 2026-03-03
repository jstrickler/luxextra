from uuid import uuid4
from django.db import models

# Create your models here.

# class MyModel(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid4, editable=False, help_text="Unique ID of this MyModel record")
#     # add other fields here...
#
#     class Meta:  # customize the model
#         db_table = 'tablename'  # optional
#         verbose_name = 'name'
#         verbose_name_plural = 'names'
#         ordering = ['field1', ...]  # use -field for descending, ? for random
#
#     def __str__(self):  # how the model is displayed
#         return self.name  # edit as needed
