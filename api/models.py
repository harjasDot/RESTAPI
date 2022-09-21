from django.db import models

# Create your models here.
STATUS_CHOICES = (
    ("1", "PENDING"),
    ("2", "ACCEPTED"),
    ("3", "REJECTED"),
)
    
class Apply(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    status=models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES,
        default = 'PENDING'
        )

    def __str__(self):
        return self.name