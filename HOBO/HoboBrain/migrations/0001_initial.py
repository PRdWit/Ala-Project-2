# Generated by Django 5.0.2 on 2024-05-08 09:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abonnement',
            fields=[
                ('aboid', models.AutoField(db_column='AboID', primary_key=True, serialize=False)),
                ('abonaam', models.CharField(blank=True, db_column='AboNaam', max_length=50, null=True)),
                ('maxdevices', models.IntegerField(blank=True, db_column='MaxDevices', null=True)),
                ('streamkwaliteit', models.IntegerField(blank=True, db_column='StreamKwaliteit', null=True)),
            ],
            options={
                'db_table': 'abonnement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Aflevering',
            fields=[
                ('afleveringid', models.AutoField(db_column='AfleveringID', primary_key=True, serialize=False)),
                ('rang', models.IntegerField(blank=True, db_column='Rang', null=True)),
                ('afltitel', models.CharField(blank=True, db_column='AflTitel', max_length=100, null=True)),
                ('duur', models.IntegerField(blank=True, db_column='Duur', null=True)),
            ],
            options={
                'db_table': 'aflevering',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genreid', models.AutoField(db_column='GenreID', primary_key=True, serialize=False)),
                ('genrenaam', models.CharField(blank=True, db_column='GenreNaam', max_length=50, null=True)),
            ],
            options={
                'db_table': 'genre',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Klant',
            fields=[
                ('klantnr', models.AutoField(db_column='KlantNr', primary_key=True, serialize=False)),
                ('voornaam', models.CharField(blank=True, db_column='Voornaam', max_length=50, null=True)),
                ('tussenvoegsel', models.CharField(blank=True, db_column='Tussenvoegsel', max_length=10, null=True)),
                ('achternaam', models.CharField(blank=True, db_column='Achternaam', max_length=50, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('genre', models.CharField(db_column='Genre', max_length=255)),
            ],
            options={
                'db_table': 'klant',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seizoen',
            fields=[
                ('seizoenid', models.AutoField(db_column='SeizoenID', primary_key=True, serialize=False)),
                ('serieid', models.IntegerField(db_column='SerieID')),
                ('rang', models.IntegerField(blank=True, db_column='Rang', null=True)),
                ('jaar', models.IntegerField(blank=True, db_column='Jaar', null=True)),
                ('imdbrating', models.IntegerField(blank=True, db_column='IMDBRating', null=True)),
            ],
            options={
                'db_table': 'seizoen',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('serieid', models.AutoField(db_column='SerieID', primary_key=True, serialize=False)),
                ('serietitel', models.CharField(blank=True, db_column='SerieTitel', max_length=100, null=True)),
                ('imdblink', models.CharField(blank=True, db_column='IMDBLink', max_length=100, null=True)),
                ('actief', models.IntegerField(blank=True, db_column='Actief', null=True)),
                ('trending', models.IntegerField(blank=True, db_column='Trending', null=True)),
                ('editorpick', models.IntegerField(blank=True, db_column='EditorPick', null=True)),
            ],
            options={
                'db_table': 'serie',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('streamid', models.AutoField(db_column='StreamID', primary_key=True, serialize=False)),
                ('d_start', models.DateTimeField(blank=True, null=True)),
                ('d_eind', models.DateTimeField(blank=True, null=True)),
                ('ip', models.CharField(blank=True, db_column='IP', max_length=20, null=True)),
            ],
            options={
                'db_table': 'stream',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SerieGenre',
            fields=[
                ('serieid', models.OneToOneField(db_column='SerieID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='HoboBrain.serie')),
            ],
            options={
                'db_table': 'serie_genre',
                'managed': False,
            },
        ),
    ]