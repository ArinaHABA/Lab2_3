from django.db import models


class Dorm(models.Model):
    dorm_id = models.IntegerField(primary_key=True)
    dorm_address = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'dorm'


class Food(models.Model):
    food_id = models.AutoField(primary_key=True)
    id_food_type = models.ForeignKey('FoodType', models.DO_NOTHING, db_column='id_food_type')
    food_name = models.CharField(unique=True, max_length=30)
    food_price = models.FloatField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    is_in_stock = models.BooleanField(blank=True, null=True)
    image = models.CharField(max_length=30, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'food'


class FoodType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food_type'


class Item(models.Model):
    id_tray = models.OneToOneField('Tray', models.DO_NOTHING, db_column='id_tray', primary_key=True)
    id_food = models.ForeignKey(Food, models.DO_NOTHING, db_column='id_food')
    amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item'
        unique_together = (('id_tray', 'id_food'),)


class Tray(models.Model):
    tray_id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user')
    id_dorm = models.ForeignKey(Dorm, models.DO_NOTHING, db_column='id_dorm')
    id_status = models.ForeignKey('TrayStatus', models.DO_NOTHING, db_column='id_status')
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tray'



class TrayStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(unique=True, max_length=1)
    description = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tray_status'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    login = models.CharField(unique=True, max_length=10)
    password = models.CharField(max_length=10)
    student_card = models.CharField(unique=True, max_length=8)

    class Meta:
        managed = False
        db_table = 'user'
