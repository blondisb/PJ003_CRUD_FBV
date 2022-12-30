from django.db import models

# Create your models here.
class MO_project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MO_task(models.Model):
    tittle = models.CharField(max_length=200)
    descrip = models.TextField()
    project = models.ForeignKey(MO_project, on_delete=models.CASCADE)
    state = models.BooleanField(default=False)

    def __str__(self):
        return self.tittle + ' - ' + self.project.name

    
class MO_deleteme(models.Model):
    name = models.CharField(max_length=100)