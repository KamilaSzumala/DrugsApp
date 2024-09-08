# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class ATC(models.Model):
    code = models.TextField(db_column='ATC', blank=True, null=False)  # Field name made lowercase.

    def __str__(self):
        return self.code



class NetherlandsDrug(models.Model):
    numer_rejestracyjny = models.TextField(db_column='NUMER REJESTRACYJNY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rodzaj = models.TextField(db_column='RODZAJ', blank=True, null=True)  # Field name made lowercase.
    nazwa_produktu = models.TextField(db_column='NAZWA PRODUKTU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    podmiot_odpowiedzialny = models.TextField(db_column='PODMIOT ODPOWIEDZIALNY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status_dostawy = models.TextField(db_column='STATUS DOSTAWY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    forma_leku = models.TextField(db_column='FORMA LEKU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trasa = models.TextField(db_column='TRASA', blank=True, null=True)  # Field name made lowercase.
    atc = models.OneToOneField(ATC, models.DO_NOTHING, primary_key=True, db_column='ATC', blank=True, null=False, default=0)  # Field name made lowercase.

    def __str__(self):
        return self.nazwa_produktu


class PolandDrug(models.Model):
    numer_rejestracyjny = models.TextField(db_column='NUMER REJESTRACYJNY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nazwa_produktu = models.TextField(db_column='NAZWA PRODUKTU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    podmiot_odpowiedzialny = models.TextField(db_column='PODMIOT ODPOWIEDZIALNY', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    forma_leku = models.TextField(db_column='FORMA LEKU', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trasa = models.TextField(db_column='TRASA', blank=True, null=True)  # Field name made lowercase.
    atc = models.OneToOneField(ATC, models.DO_NOTHING, primary_key=True, db_column='ATC', blank=True, null=False, default=0)  # Field name made lowercase.

    def __str__(self):
        return self.nazwa_produktu