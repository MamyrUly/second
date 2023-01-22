from django.db import models

class Articles(models.Model):
    title = models.CharField('Thisis news bteo', max_length=100)
    anons = models.CharField('anons', max_length=120)
    full_text = models.TextField('article')
    date = models.DateTimeField('data of submition')

    def __str__(self):
        return self.title