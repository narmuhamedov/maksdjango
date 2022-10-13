from django.db import models

CHOISE = (
    ('HORROR', 'HORROR'),
    ('COMEDY', 'COMEDY'),
    ('MELODRAMME', 'MELODRAMME'),
    ('HISTORY', 'HISTORY'),
    ('ADVENTURE', 'ADVENTURE'),
    ('ANIME', 'ANIME')
)

class TVShow(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    quantity = models.IntegerField()
    genre = models.CharField(choices=CHOISE, max_length=100)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
