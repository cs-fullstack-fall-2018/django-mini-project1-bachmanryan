from django.db import models
from django.utils import timezone


class Post(models.Model):
    name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    school = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    hours = models.IntegerField()
    date_of_work = models.IntegerField()
    date_of_entry = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.school
