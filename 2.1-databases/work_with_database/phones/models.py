from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.FilePathField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=100, db_index=True, verbose_name='URL')


