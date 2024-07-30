from django.db import models
import uuid
from datetime import datetime

# Create your models here.
class Alert(models.Model):
    id = models.UUIDField(primary_key=True,default = uuid.uuid4, editable = False)
    status = models.CharField(max_length=80,default='CREATED')
    created = models.DateTimeField(default=datetime.now)
    username = models.CharField(max_length=80)
    amount = models.FloatField()
    currentPrice = models.FloatField()