from django.db import models


class Abonnement(models.Model):
    aboid = models.AutoField(db_column='AboID', primary_key=True)  # Field name made lowercase.
    abonaam = models.CharField(db_column='AboNaam', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maxdevices = models.IntegerField(db_column='MaxDevices', blank=True, null=True)  # Field name made lowercase.
    streamkwaliteit = models.IntegerField(db_column='StreamKwaliteit', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'abonnement'
        verbose_name_plural = "Abonnoment"


class Aflevering(models.Model):
    afleveringid = models.AutoField(db_column='AfleveringID', primary_key=True)  # Field name made lowercase.
    seizid = models.ForeignKey('Seizoen', models.DO_NOTHING, db_column='SeizID')  # Field name made lowercase.
    rang = models.IntegerField(db_column='Rang', blank=True, null=True)  # Field name made lowercase.
    afltitel = models.CharField(db_column='AflTitel', max_length=100, blank=True, null=True)  # Field name made lowercase.
    duur = models.IntegerField(db_column='Duur', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aflevering'
        verbose_name_plural = "Aflevering"


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'
        verbose_name_plural = "AuthGroup"


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)
        verbose_name_plural = "AuthGroupPermission"


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)
        verbose_name_plural = "AuthPermission"


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'
        verbose_name_plural = "AuthUser"


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)
        verbose_name_plural = "AuthUserGroups"


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)
        verbose_name_plural = "AuthUserUserPermissions"


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
        verbose_name_plural = "DjangoMigrations"
        


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Genre(models.Model):
    genreid = models.AutoField(db_column='GenreID', primary_key=True)  # Field name made lowercase.
    genrenaam = models.CharField(db_column='GenreNaam', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'genre'


class Klant(models.Model):
    klantnr = models.AutoField(db_column='KlantNr', primary_key=True)  # Field name made lowercase.
    aboid = models.ForeignKey(Abonnement, models.DO_NOTHING, db_column='AboID')  # Field name made lowercase.
    voornaam = models.CharField(db_column='Voornaam', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tussenvoegsel = models.CharField(db_column='Tussenvoegsel', max_length=10, blank=True, null=True)  # Field name made lowercase.
    achternaam = models.CharField(db_column='Achternaam', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(db_column='Genre', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'klant'
        verbose_name_plural = "Klant"


class Seizoen(models.Model):
    seizoenid = models.AutoField(db_column='SeizoenID', primary_key=True)  # Field name made lowercase.
    serieid = models.IntegerField(db_column='SerieID')  # Field name made lowercase.
    rang = models.IntegerField(db_column='Rang', blank=True, null=True)  # Field name made lowercase.
    jaar = models.IntegerField(db_column='Jaar', blank=True, null=True)  # Field name made lowercase.
    imdbrating = models.IntegerField(db_column='IMDBRating', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'seizoen'
        verbose_name_plural = "Seizoen"


class Serie(models.Model):
    serieid = models.AutoField(db_column='SerieID', primary_key=True)  # Field name made lowercase.
    serietitel = models.CharField(db_column='SerieTitel', max_length=100, blank=True, null=True)  # Field name made lowercase.
    imdblink = models.CharField(db_column='IMDBLink', max_length=100, blank=True, null=True)  # Field name made lowercase.
    actief = models.IntegerField(db_column='Actief', blank=True, null=True)  # Field name made lowercase.
    trending = models.IntegerField(db_column='Trending', blank=True, null=True)
    editorpick = models.IntegerField(db_column='EditorPick', blank=True, null=True)
    act_imbdlink = models.CharField(db_column='Act_imbdlink', max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serie'


class SerieGenre(models.Model):
    serieid = models.OneToOneField(Serie, models.DO_NOTHING, db_column='SerieID', primary_key=True)  # Field name made lowercase. The composite primary key (SerieID, GenreID) found, that is not supported. The first column is selected.
    genreid = models.ForeignKey(Genre, models.DO_NOTHING, db_column='GenreID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'serie_genre'
        unique_together = (('serieid', 'genreid'),)


class Stream(models.Model):
    streamid = models.AutoField(db_column='StreamID', primary_key=True)  # Field name made lowercase.
    klantid = models.ForeignKey(Klant, models.DO_NOTHING, db_column='KlantID')  # Field name made lowercase.
    aflid = models.ForeignKey(Aflevering, models.DO_NOTHING, db_column='AflID')  # Field name made lowercase.
    d_start = models.DateTimeField(blank=True, null=True)
    d_eind = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(db_column='IP', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stream'
        verbose_name_plural = "Stream"


class Users(models.Model):
    username = models.CharField(unique=True, max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users'
        verbose_name_plural = "Users"