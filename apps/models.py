from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} - {self.name}'


class District(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
