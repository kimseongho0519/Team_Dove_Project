from django.db import models


class Aluminium(models.Model):
    날짜 = models.DateField(blank=True, null=True)
    가격 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aluminium'


class DomesticOil(models.Model):
    날짜 = models.DateField(blank=True, null=True)
    고급휘발유 = models.FloatField(blank=True, null=True)
    보통휘발유 = models.FloatField(blank=True, null=True)
    자동차용경유 = models.FloatField(blank=True, null=True)
    실내등유 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'domestic_oil'


class Grain(models.Model):
    날짜 = models.DateField(blank=True, null=True)
    곡류 = models.CharField(max_length=10, blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    정착가 = models.FloatField(blank=True, null=True)
    양 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grain'


class MonthlyAl(models.Model):
    날짜 = models.TextField(blank=True, null=True)
    알루미늄 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monthly_al'


class MonthlyDomesticOil(models.Model):
    날짜 = models.TextField(blank=True, null=True)
    고급휘발유 = models.FloatField(blank=True, null=True)
    보통휘발유 = models.FloatField(blank=True, null=True)
    자동차용경유 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monthly_domestic_oil'


class MonthlyGrain(models.Model):
    날짜 = models.TextField(blank=True, null=True)
    대두 = models.FloatField(blank=True, null=True)
    밀 = models.FloatField(blank=True, null=True)
    옥수수 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monthly_grain'


class MonthlyOverseaOil(models.Model):
    날짜 = models.TextField(blank=True, null=True)
    휘발유_95ron = models.FloatField(db_column='휘발유_95RON', blank=True, null=True)  # Field name made lowercase.
    휘발유_92ron = models.FloatField(db_column='휘발유_92RON', blank=True, null=True)  # Field name made lowercase.
    경유0001 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monthly_oversea_oil'


class OverseaOil(models.Model):
    날짜 = models.DateField(blank=True, null=True)
    휘발유_95ron = models.FloatField(blank=True, null=True)
    휘발유_92ron = models.FloatField(blank=True, null=True)
    등유 = models.FloatField(blank=True, null=True)
    경유005 = models.FloatField(blank=True, null=True)
    경유0001 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oversea_oil'
