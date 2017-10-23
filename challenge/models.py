from django.db import models


# Create your models here.

class FoodCategory(models.Model):
    class Meta:
        db_table = "food_category"

    _id = models.IntegerField(primary_key=True)
    food_category_short_name = models.CharField(max_length=3)
    food_category_long_name = models.CharField(max_length=50)


class FoodDetailCategory(models.Model):
    class Meta:
        db_table = "food_detail_category"

    _id = models.IntegerField(primary_key=True)
    food_category_id = models.ForeignKey(FoodCategory, db_column='food_category_id')
    # food_category_id = models.IntegerField()
    description = models.CharField(max_length=50)


class FoodEntry(models.Model):
    class Meta:
        db_table = "foodentry"

    _id = models.AutoField(primary_key=True)
    food_detail_category_id = models.ForeignKey(FoodDetailCategory, db_column='food_detail_category_id')
    food_category_id = models.ForeignKey(FoodCategory, db_column='food_category_id', default=0)
    # food_detail_category_id = models.IntegerField()
    # food_category_id = models.IntegerField(default=0)
    serving_size = models.CharField(max_length=100)
    food_name = models.CharField(max_length=100)


class Serving(models.Model):
    class Meta:
        db_table = "serving"
        # unique_together = ('food_category_id','gender','age_lower','age_upper')

    _id = models.AutoField(primary_key=True)
    food_category_id = models.ForeignKey(FoodCategory, db_column='food_category_id')
    # food_category_id = models.IntegerField()
    gender = models.CharField(max_length=10)
    age_lower = models.IntegerField()
    age_upper = models.IntegerField()
    serving_number = models.CharField(null=False, max_length=20)


class DirectionalStatement(models.Model):
    class Meta:
        db_table = "directional_statement"

    _id = models.AutoField(primary_key=True)
    food_category_id = models.ForeignKey(FoodCategory, db_column='food_category_id')
    # food_category_id = models.IntegerField()
    statement = models.CharField(max_length=100)
