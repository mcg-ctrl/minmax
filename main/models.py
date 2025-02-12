from django.db import models


# Create your models here.

class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, default='')
    seller = models.CharField(max_length=200, default='')
    price = models.FloatField()
    quantity = models.IntegerField(default=1)   # Default: positive one

    servings_per_cont = models.IntegerField(default=1)
    serving_size = models.FloatField(default=1)
    mass = models.FloatField(default=1)   # total mass, i.e. servings_val*serving_size
    flavor = models.IntegerField()
    favorite = models.BooleanField(default=False)

    # The following parameters have "amount per serving" values:
    calories = models.FloatField()
    total_fat = models.FloatField()
    sat_fat = models.FloatField()
    trans_fat = models.FloatField()
    cholesterol = models.FloatField()
    sodium = models.FloatField()
    carbs = models.FloatField()
    fiber = models.FloatField()
    total_sugar = models.FloatField()
    added_sugar = models.FloatField()
    protein = models.FloatField()

    def __str__(self):
        print_name = self.brand + ' ' + self.name
        return print_name