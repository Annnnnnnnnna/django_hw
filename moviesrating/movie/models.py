from django.db import models

# Create your models here.
class Movies(models.Model):
    movie_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=191, blank=True, null=True)
    genres = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies'


class Ratings(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    movie_id = models.IntegerField()
    rating = models.FloatField()
    class Meta:
        managed = False
        db_table = 'ratings'