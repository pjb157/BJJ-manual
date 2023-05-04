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
    description = models.CharField(max_length=200, null=True, blank=True)
    video_link = models.URLField(null=True, blank=True)
    is_attacking = models.BooleanField(default=False)
    is_defending = models.BooleanField(default=False)
    # image = models.URLField

    def __str__(self):
        return self.name
    
class Step(models.Model):
    name = models.CharField(max_length=100)
    move = models.ForeignKey(Move, on_delete=models.CASCADE, related_name="steps")
    step_order = models.IntegerField(null=False)

    def __str__(self):
        return self.name