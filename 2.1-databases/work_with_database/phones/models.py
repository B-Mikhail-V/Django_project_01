from django.db import models


class Phone(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.FilePathField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=100, blank=True)

    def __str__(self):
        return self.name
