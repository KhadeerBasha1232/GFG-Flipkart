from django.db import models

# Create your models here.
from django.db import models

class Problem(models.Model):
    name = models.CharField(max_length=255)
    submission_id = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)  # Add this field

    def __str__(self):
        return self.name