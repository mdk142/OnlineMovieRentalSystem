# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_authgrouppermissions_authtokentoken_authusergroups'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('user', models.ForeignKey(to='myapp.AuthUser', to_field='id')),
                ('permission', models.ForeignKey(to='myapp.AuthPermission', to_field='id')),
            ],
            options={
                u'db_table': u'auth_user_user_permissions',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('action_time', models.DateTimeField()),
                ('user', models.ForeignKey(to='myapp.AuthUser', to_field='id')),
                ('content_type', models.ForeignKey(to_field='id', blank=True, to='myapp.DjangoContentType', null=True)),
                ('object_id', models.TextField(blank=True)),
                ('object_repr', models.CharField(max_length=400, blank=True)),
                ('action_flag', models.IntegerField()),
                ('change_message', models.TextField(blank=True)),
            ],
            options={
                u'db_table': u'django_admin_log',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MainChoice',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('poll', models.ForeignKey(to='myapp.MainPoll', to_field='id')),
                ('choice_text', models.CharField(max_length=400, blank=True)),
                ('votes', models.IntegerField()),
            ],
            options={
                u'db_table': u'main_choice',
                u'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
