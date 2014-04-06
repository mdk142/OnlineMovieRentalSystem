# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Actor(models.Model):
    actor_id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'actor'

class Cast(models.Model):
    actor = models.ForeignKey(Actor)
    movie = models.ForeignKey('Movie')
    role = models.CharField(max_length=30)
    class Meta:
        managed = False
        db_table = 'cast'

class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    director_id = models.FloatField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'director'

class Genres(models.Model):
    movie_id = models.CharField(max_length=50)
    genre = models.CharField(max_length=25)
    class Meta:
        managed = False
        db_table = 'genres'

class Movie(models.Model):
    movie_id = models.BigIntegerField(primary_key=True)
    year = models.IntegerField()
    movie_name = models.CharField(max_length=75)
    class Meta:
        managed = False
        db_table = 'movie'

class MovieDirector(models.Model):
    director = models.ForeignKey(Director)
    movie = models.ForeignKey(Movie)
    class Meta:
        managed = False
        db_table = 'movie_director'

