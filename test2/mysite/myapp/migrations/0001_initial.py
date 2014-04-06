# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('app_label', models.CharField(max_length=200, blank=True)),
                ('model', models.CharField(max_length=200, blank=True)),
            ],
            options={
                u'db_table': u'django_content_type',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='River',
            fields=[
                ('name', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('river', models.CharField(max_length=40, blank=True)),
                ('lake', models.CharField(max_length=40, blank=True)),
                ('sea', models.CharField(max_length=40, blank=True)),
                ('length', models.FloatField(null=True, blank=True)),
                ('source', models.TextField(blank=True)),
                ('mountains', models.CharField(max_length=40, blank=True)),
                ('sourceelevation', models.FloatField(null=True, blank=True)),
                ('estuary', models.TextField(blank=True)),
            ],
            options={
                u'db_table': u'river',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Encompasses',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=4)),
                ('continent', models.CharField(max_length=20)),
                ('percentage', models.FloatField(null=True, blank=True)),
            ],
            options={
                u'db_table': u'encompasses',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('abbreviation', models.CharField(max_length=12, serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80)),
                ('city', models.CharField(max_length=40, blank=True)),
                ('country', models.CharField(max_length=4, blank=True)),
                ('province', models.CharField(max_length=40, blank=True)),
                ('established', models.DateField(null=True, blank=True)),
            ],
            options={
                u'db_table': u'organization',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=160, blank=True)),
            ],
            options={
                u'db_table': u'auth_group',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Desert',
            fields=[
                ('name', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('area', models.FloatField(null=True, blank=True)),
                ('coordinates', models.TextField(blank=True)),
            ],
            options={
                u'db_table': u'desert',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mountain',
            fields=[
                ('name', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('mountains', models.CharField(max_length=40, blank=True)),
                ('elevation', models.FloatField(null=True, blank=True)),
                ('type', models.CharField(max_length=10, blank=True)),
                ('coordinates', models.TextField(blank=True)),
            ],
            options={
                u'db_table': u'mountain',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GeoSea',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('sea', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=4)),
                ('province', models.CharField(max_length=40)),
            ],
            options={
                u'db_table': u'geo_sea',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=256, blank=True)),
                ('last_login', models.DateTimeField()),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(unique=True, max_length=60, blank=True)),
                ('first_name', models.CharField(max_length=60, blank=True)),
                ('last_name', models.CharField(max_length=60, blank=True)),
                ('email', models.CharField(max_length=150, blank=True)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                u'db_table': u'auth_user',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AppAddress',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('street', models.CharField(max_length=400, blank=True)),
                ('city', models.CharField(max_length=400, blank=True)),
                ('state', models.CharField(max_length=400, blank=True)),
                ('country', models.CharField(max_length=400, blank=True)),
            ],
            options={
                u'db_table': u'app_address',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lake',
            fields=[
                ('name', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('area', models.FloatField(null=True, blank=True)),
                ('depth', models.FloatField(null=True, blank=True)),
                ('elevation', models.FloatField(null=True, blank=True)),
                ('type', models.CharField(max_length=12, blank=True)),
                ('river', models.CharField(max_length=40, blank=True)),
                ('coordinates', models.TextField(blank=True)),
            ],
            options={
                u'db_table': u'lake',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Borders',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('country1', models.CharField(max_length=4)),
                ('country2', models.CharField(max_length=4)),
                ('length', models.FloatField(null=True, blank=True)),
            ],
            options={
                u'db_table': u'borders',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GeoSource',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('river', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=4)),
                ('province', models.CharField(max_length=40)),
            ],
            options={
                u'db_table': u'geo_source',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movie1',
            fields=[
                ('movieid', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30, blank=True)),
                ('rated', models.CharField(max_length=10, blank=True)),
                ('category', models.CharField(max_length=10, blank=True)),
                ('releasedata', models.DateField(null=True, blank=True)),
                ('length', models.IntegerField(null=True, blank=True)),
            ],
            options={
                u'db_table': u'movie1',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movieid', models.FloatField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=40, blank=True)),
                ('rated', models.CharField(max_length=5, blank=True)),
                ('category', models.CharField(max_length=10, blank=True)),
                ('releasedata', models.DateField(null=True, blank=True)),
                ('length', models.FloatField(null=True, blank=True)),
            ],
            options={
                u'db_table': u'movie',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GeoLake',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('lake', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=4)),
                ('province', models.CharField(max_length=40)),
            ],
            options={
                u'db_table': u'geo_lake',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Economy',
            fields=[
                ('country', models.CharField(max_length=4, serialize=False, primary_key=True)),
                ('gdp', models.FloatField(null=True, blank=True)),
                ('agriculture', models.FloatField(null=True, blank=True)),
                ('service', models.FloatField(null=True, blank=True)),
                ('industry', models.FloatField(null=True, blank=True)),
                ('inflation', models.FloatField(null=True, blank=True)),
            ],
            options={
                u'db_table': u'economy',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ethnicgroup',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=50)),
                ('percentage', models.FloatField(null=True, blank=True)),
            ],
            options={
                u'db_table': u'ethnicgroup',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Locatedon',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=40)),
                ('province', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=4)),
                ('island', models.CharField(max_length=40)),
            ],
            options={
                u'db_table': u'locatedon',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('addr_id', models.IntegerField(serialize=False, primary_key=True)),
                ('street', models.CharField(max_length=20, blank=True)),
                ('city', models.CharField(max_length=20, blank=True)),
                ('state', models.CharField(max_length=10, blank=True)),
                ('country', models.CharField(max_length=10, blank=True)),
            ],
            options={
                u'db_table': u'address',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Riverthrough',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('river', models.CharField(max_length=40)),
                ('lake', models.CharField(max_length=40)),
            ],
            options={
                u'db_table': u'riverthrough',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SouthMigrationhistory',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('app_name', models.CharField(max_length=510, blank=True)),
                ('migration', models.CharField(max_length=510, blank=True)),
                ('applied', models.DateTimeField()),
            ],
            options={
                u'db_table': u'south_migrationhistory',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GeoRiver',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('river', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=4)),
                ('province', models.CharField(max_length=40)),
            ],
            options={
                u'db_table': u'geo_river',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=80, serialize=False, primary_key=True)),
                ('session_data', models.TextField(blank=True)),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                u'db_table': u'django_session',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GeoMountain',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('mountain', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=4)),
                ('province', models.CharField(max_length=40)),
            ],
            options={
                u'db_table': u'geo_mountain',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('app', models.CharField(max_length=510, blank=True)),
                ('name', models.CharField(max_length=510, blank=True)),
                ('applied', models.DateTimeField()),
            ],
            options={
                u'db_table': u'django_migrations',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Island',
            fields=[
                ('name', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('islands', models.CharField(max_length=40, blank=True)),
                ('area', models.FloatField(null=True, blank=True)),
                ('elevation', models.FloatField(null=True, blank=True)),
                ('type', models.CharField(max_length=10, blank=True)),
                ('coordinates', models.TextField(blank=True)),
            ],
            options={
                u'db_table': u'island',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('name', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('area', models.IntegerField(null=True, blank=True)),
            ],
            options={
                u'db_table': u'continent',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Located',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=40, blank=True)),
                ('province', models.CharField(max_length=40, blank=True)),
                ('country', models.CharField(max_length=4, blank=True)),
                ('river', models.CharField(max_length=40, blank=True)),
                ('lake', models.CharField(max_length=40, blank=True)),
                ('sea', models.CharField(max_length=40, blank=True)),
            ],
            options={
                u'db_table': u'located',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Population',
            fields=[
                ('country', models.CharField(max_length=4, serialize=False, primary_key=True)),
                ('population_growth', models.FloatField(null=True, blank=True)),
                ('infant_mortality', models.FloatField(null=True, blank=True)),
            ],
            options={
                u'db_table': u'population',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Politics',
            fields=[
                ('country', models.CharField(max_length=4, serialize=False, primary_key=True)),
                ('independence', models.DateField(null=True, blank=True)),
                ('wasdependent', models.CharField(max_length=40, blank=True)),
                ('dependent', models.CharField(max_length=4, blank=True)),
                ('government', models.CharField(max_length=120, blank=True)),
            ],
            options={
                u'db_table': u'politics',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MainPoll',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('question', models.CharField(max_length=400, blank=True)),
                ('pub_date', models.DateTimeField()),
            ],
            options={
                u'db_table': u'main_poll',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=4)),
                ('province', models.CharField(max_length=40)),
                ('population', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('elevation', models.FloatField(null=True, blank=True)),
            ],
            options={
                u'db_table': u'city',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sea',
            fields=[
                ('name', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('depth', models.FloatField(null=True, blank=True)),
            ],
            options={
                u'db_table': u'sea',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=50)),
                ('percentage', models.FloatField(null=True, blank=True)),
            ],
            options={
                u'db_table': u'religion',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ismember',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=4)),
                ('organization', models.CharField(max_length=12)),
                ('type', models.CharField(max_length=40, blank=True)),
            ],
            options={
                u'db_table': u'ismember',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GeoIsland',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('island', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=4)),
                ('province', models.CharField(max_length=40)),
            ],
            options={
                u'db_table': u'geo_island',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GeoEstuary',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('river', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=4)),
                ('province', models.CharField(max_length=40)),
            ],
            options={
                u'db_table': u'geo_estuary',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('name', models.CharField(unique=True, max_length=40)),
                ('code', models.CharField(max_length=4, serialize=False, primary_key=True)),
                ('capital', models.CharField(max_length=40, blank=True)),
                ('province', models.CharField(max_length=40, blank=True)),
                ('area', models.FloatField(null=True, blank=True)),
                ('population', models.FloatField(null=True, blank=True)),
            ],
            options={
                u'db_table': u'country',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movie0',
            fields=[
                ('movieid', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30, blank=True)),
            ],
            options={
                u'db_table': u'movie0',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GeoDesert',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('desert', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=4)),
                ('province', models.CharField(max_length=40)),
            ],
            options={
                u'db_table': u'geo_desert',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=50)),
                ('percentage', models.FloatField(null=True, blank=True)),
            ],
            options={
                u'db_table': u'language',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=4)),
                ('population', models.FloatField(null=True, blank=True)),
                ('area', models.FloatField(null=True, blank=True)),
                ('capital', models.CharField(max_length=40, blank=True)),
                ('capprov', models.CharField(max_length=40, blank=True)),
            ],
            options={
                u'db_table': u'province',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mergeswith',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('sea1', models.CharField(max_length=40)),
                ('sea2', models.CharField(max_length=40)),
            ],
            options={
                u'db_table': u'mergeswith',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Islandin',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('island', models.CharField(max_length=40, blank=True)),
                ('sea', models.CharField(max_length=40, blank=True)),
                ('lake', models.CharField(max_length=40, blank=True)),
                ('river', models.CharField(max_length=40, blank=True)),
            ],
            options={
                u'db_table': u'islandin',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mountainonisland',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('mountain', models.CharField(max_length=40)),
                ('island', models.CharField(max_length=40)),
            ],
            options={
                u'db_table': u'mountainonisland',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, blank=True)),
                ('content_type', models.ForeignKey(to='myapp.DjangoContentType', to_field='id')),
                ('codename', models.CharField(max_length=200, blank=True)),
            ],
            options={
                u'db_table': u'auth_permission',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
