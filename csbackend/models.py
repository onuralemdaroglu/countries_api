from django.db import models

# Create your models here.
class Countries(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.id