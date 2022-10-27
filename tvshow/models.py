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
    trailers_film = models.URLField(null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class About_Us(models.Model):
    img = models.ImageField(upload_to='')
    description = models.TextField()
    work_year = models.IntegerField(max_length=20)

    def __str__(self):
        return self.description

