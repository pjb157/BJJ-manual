from django.db import models

# Create your models here.
class Position(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Move(models.Model):
    name = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name="moves")

    def __str__(self):
        return self.name