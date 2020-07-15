from django.db import models


# =========== CLASS - models / DB table
class DjangoClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=False, null=False)
    courseNumber = models.IntegerField()
    instructorName = models.CharField(max_length=60, default="", blank=True, null=True)
    duration = models.DecimalField(default=0.0, max_digits=100, decimal_places=1)

    objects = models.Manager()

    def __str__(self):
        return self.title
