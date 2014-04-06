# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('group', models.ForeignKey(to='myapp.AuthGroup', to_field='id')),
                ('permission', models.ForeignKey(to='myapp.AuthPermission', to_field='id')),
            ],
            options={
                u'db_table': u'auth_group_permissions',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthtokenToken',
            fields=[
                ('key', models.CharField(max_length=80, serialize=False, primary_key=True)),
                ('user', models.ForeignKey(to='myapp.AuthUser', to_field='id', unique=True)),
                ('created', models.DateTimeField()),
            ],
            options={
                u'db_table': u'authtoken_token',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('user', models.ForeignKey(to='myapp.AuthUser', to_field='id')),
                ('group', models.ForeignKey(to='myapp.AuthGroup', to_field='id')),
            ],
            options={
                u'db_table': u'auth_user_groups',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
