# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Address(models.Model):
    addr_id = models.IntegerField(primary_key=True)
    street = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=10, blank=True)

    class Meta:
        managed = False
        db_table = 'address'


class AppAddress(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    street = models.CharField(max_length=400, blank=True)
    city = models.CharField(max_length=400, blank=True)
    state = models.CharField(max_length=400, blank=True)
    country = models.CharField(max_length=400, blank=True)

    class Meta:
        managed = False
        db_table = 'app_address'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=160, blank=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100, blank=True)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=256, blank=True)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=60, blank=True)
    first_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60, blank=True)
    email = models.CharField(max_length=150, blank=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=80)
    user = models.ForeignKey(AuthUser, unique=True)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Borders(models.Model):
    country1 = models.CharField(max_length=4)
    country2 = models.CharField(max_length=4)
    length = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'borders'


class City(models.Model):
    name = models.CharField(max_length=40)
    country = models.CharField(max_length=4)
    province = models.CharField(max_length=40)
    population = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    elevation = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'


class Continent(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    area = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'continent'


class Country(models.Model):
    name = models.CharField(unique=True, max_length=40)
    code = models.CharField(primary_key=True, max_length=4)
    capital = models.CharField(max_length=40, blank=True)
    province = models.CharField(max_length=40, blank=True)
    area = models.FloatField(blank=True, null=True)
    population = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class Desert(models.Model):
    name = models.CharField(primary_key=True, max_length=40)
    area = models.FloatField(blank=True, null=True)
    coordinates = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'desert'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=400, blank=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=200, blank=True)
    app_label = models.CharField(max_length=200, blank=True)
    model = models.CharField(max_length=200, blank=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=510, blank=True)
    name = models.CharField(max_length=510, blank=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=80)
    session_data = models.TextField(blank=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Economy(models.Model):
    country = models.CharField(primary_key=True, max_length=4)
    gdp = models.FloatField(blank=True, null=True)
    agriculture = models.FloatField(blank=True, null=True)
    service = models.FloatField(blank=True, null=True)
    industry = models.FloatField(blank=True, null=True)
    inflation = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'economy'


class Encompasses(models.Model):
    country = models.CharField(max_length=4)
    continent = models.CharField(max_length=20)
    percentage = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'encompasses'


class Ethnicgroup(models.Model):
    country = models.CharField(max_length=4)
    name = models.CharField(max_length=50)
    percentage = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ethnicgroup'


class GeoDesert(models.Model):
    desert = models.CharField(max_length=40)
    country = models.CharField(max_length=4)
    province = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'geo_desert'


class GeoEstuary(models.Model):
    river = models.CharField(max_length=40)
    country = models.CharField(max_length=4)
    province = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'geo_estuary'


class GeoIsland(models.Model):
    island = models.CharField(max_length=40)
    country = models.CharField(max_length=4)
    province = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'geo_island'


class GeoLake(models.Model):
    lake = models.CharField(max_length=40)
    country = models.CharField(max_length=4)
    province = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'geo_lake'


class GeoMountain(models.Model):
    mountain = models.CharField(max_length=40)
    country = models.CharField(max_length=4)
    province = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'geo_mountain'


class GeoRiver(models.Model):
    river = models.CharField(max_length=40)
    country = models.CharField(max_length=4)
    province = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'geo_river'


class GeoSea(models.Model):
    sea = models.CharField(max_length=40)
    country = models.CharField(max_length=4)
    province = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'geo_sea'


class GeoSource(models.Model):
    river = models.CharField(max_length=40)
    country = models.CharField(max_length=4)
    province = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'geo_source'


class Island(models.Model):
    name = models.CharField(primary_key=True, max_length=40)
    islands = models.CharField(max_length=40, blank=True)
    area = models.FloatField(blank=True, null=True)
    elevation = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=10, blank=True)
    coordinates = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'island'


class Islandin(models.Model):
    island = models.CharField(max_length=40, blank=True)
    sea = models.CharField(max_length=40, blank=True)
    lake = models.CharField(max_length=40, blank=True)
    river = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'islandin'


class Ismember(models.Model):
    country = models.CharField(max_length=4)
    organization = models.CharField(max_length=12)
    type = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'ismember'


class Lake(models.Model):
    name = models.CharField(primary_key=True, max_length=40)
    area = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    elevation = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=12, blank=True)
    river = models.CharField(max_length=40, blank=True)
    coordinates = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'lake'


class Language(models.Model):
    country = models.CharField(max_length=4)
    name = models.CharField(max_length=50)
    percentage = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'language'


class Located(models.Model):
    city = models.CharField(max_length=40, blank=True)
    province = models.CharField(max_length=40, blank=True)
    country = models.CharField(max_length=4, blank=True)
    river = models.CharField(max_length=40, blank=True)
    lake = models.CharField(max_length=40, blank=True)
    sea = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'located'


class Locatedon(models.Model):
    city = models.CharField(max_length=40)
    province = models.CharField(max_length=40)
    country = models.CharField(max_length=4)
    island = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'locatedon'


class MainChoice(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    poll = models.ForeignKey('MainPoll')
    choice_text = models.CharField(max_length=400, blank=True)
    votes = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'main_choice'


class MainPoll(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    question = models.CharField(max_length=400, blank=True)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'main_poll'


class Mergeswith(models.Model):
    sea1 = models.CharField(max_length=40)
    sea2 = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'mergeswith'


class Mountain(models.Model):
    name = models.CharField(primary_key=True, max_length=40)
    mountains = models.CharField(max_length=40, blank=True)
    elevation = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=10, blank=True)
    coordinates = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'mountain'


class Mountainonisland(models.Model):
    mountain = models.CharField(max_length=40)
    island = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'mountainonisland'


class Movie(models.Model):
    movieid = models.FloatField(primary_key=True)
    name = models.CharField(max_length=40, blank=True)
    rated = models.CharField(max_length=5, blank=True)
    category = models.CharField(max_length=10, blank=True)
    releasedata = models.DateField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie'


class Movie0(models.Model):
    movieid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True)

    class Meta:
        managed = False
        db_table = 'movie0'


class Movie1(models.Model):
    movieid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True)
    rated = models.CharField(max_length=10, blank=True)
    category = models.CharField(max_length=10, blank=True)
    releasedata = models.DateField(blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie1'


class Organization(models.Model):
    abbreviation = models.CharField(primary_key=True, max_length=12)
    name = models.CharField(unique=True, max_length=80)
    city = models.CharField(max_length=40, blank=True)
    country = models.CharField(max_length=4, blank=True)
    province = models.CharField(max_length=40, blank=True)
    established = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organization'


class Politics(models.Model):
    country = models.CharField(primary_key=True, max_length=4)
    independence = models.DateField(blank=True, null=True)
    wasdependent = models.CharField(max_length=40, blank=True)
    dependent = models.CharField(max_length=4, blank=True)
    government = models.CharField(max_length=120, blank=True)

    class Meta:
        managed = False
        db_table = 'politics'


class Population(models.Model):
    country = models.CharField(primary_key=True, max_length=4)
    population_growth = models.FloatField(blank=True, null=True)
    infant_mortality = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'population'


class Province(models.Model):
    name = models.CharField(max_length=40)
    country = models.CharField(max_length=4)
    population = models.FloatField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    capital = models.CharField(max_length=40, blank=True)
    capprov = models.CharField(max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'province'


class Religion(models.Model):
    country = models.CharField(max_length=4)
    name = models.CharField(max_length=50)
    percentage = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'religion'


class River(models.Model):
    name = models.CharField(primary_key=True, max_length=40)
    river = models.CharField(max_length=40, blank=True)
    lake = models.CharField(max_length=40, blank=True)
    sea = models.CharField(max_length=40, blank=True)
    length = models.FloatField(blank=True, null=True)
    source = models.TextField(blank=True)  # This field type is a guess.
    mountains = models.CharField(max_length=40, blank=True)
    sourceelevation = models.FloatField(blank=True, null=True)
    estuary = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'river'


class Riverthrough(models.Model):
    river = models.CharField(max_length=40)
    lake = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'riverthrough'


class Sea(models.Model):
    name = models.CharField(primary_key=True, max_length=40)
    depth = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sea'


class SouthMigrationhistory(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_name = models.CharField(max_length=510, blank=True)
    migration = models.CharField(max_length=510, blank=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'south_migrationhistory'
