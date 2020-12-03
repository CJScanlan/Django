from django.db import models

class djangoClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    courseID = models.IntegerField(default=0, primary_key=True, max_length=5)
    instructor = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.DecimalField(default=0.0, max_digits=10000, decimal_places=2)

    objects = models.Manager()

    def __str__(self):
        return self.title
