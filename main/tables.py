import django_tables2 as tables
from .models import FoodItem

class FoodItemTable(tables.Table):

    id = tables.Column()
    name = tables.Column()
    brand = tables.Column()
    seller = tables.Column()
    price = tables.Column()
    quantity = tables.Column()
    servings_per_cont = tables.Column()
    serving_size = tables.Column()
    flavor = tables.Column()
    favorite = tables.Column()

    class Meta:
        model = FoodItem