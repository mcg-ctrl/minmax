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

class MinSettings(models.Model):

    # The minimizing factor: name (chosen from dropdown input), value limit, item's unit
    min_var = models.CharField(max_length=20)
    min_limit = models.FloatField()
    mini_units = models.CharField(max_length=5)

    min_choices = (
        ('minvalue1', 'MinLabel 1'),
        ('minvalue2', 'MinLabel 2'),
        ('minvalue3', 'MinLabel 3'),
    )

    min_field = models.CharField(max_length=20, choices=min_choices)

class MaxSettings(models.Model):

    # The maximizing factor: name (chosen from dropdown input)
    max_var = models.CharField(max_length=200)

    max_choices = (
        ('maxvalue1', 'MaxLabel 1'),
        ('maxvalue2', 'MaxLabel 2'),
        ('maxvalue3', 'MaxLabel 3'),
    )

    max_field = models.CharField(max_length=20, choices=max_choices)

    # Custom set of FoodItem items to use for the optimization
    # Button that opens page with all saved FoodItem items,
    # and allows the user to select/unselect items,
    # if they prefer to have a limit/max for each item (e.g. include
    # at most two cookies in the optimized set)
    custom_set_items = models.BooleanField(default=False)

