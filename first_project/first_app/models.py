from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length = 264, unique = True) #creating a column

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length = 264, unique = True)
    url = models.URLField(unique = True)

    def __str__(self):
        return self.name

class AccessRecords(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.DO_NOTHING,)
    date = models.DateField()

    def __str__(self):
        return self(self.date)
