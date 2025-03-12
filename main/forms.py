from django import forms
from django.forms import ModelForm
from .models import FoodItem
from .models import MinSettings
from .models import MaxSettings


class BaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for bound_field in self:
            if hasattr(bound_field, "field") and bound_field.field.required:
                bound_field.field.widget.attrs["required"] = "required"


# Class for entering a new item into the database
# with structure/form of the 'FoodItem' model
# and all its attributes (hence: '__all__')
class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = '__all__'

class MinMaxForm(forms.Form):
    min_choices = (
        ('price', 'Price'),
        ('calories', 'Calories'),
    )

    max_choices = (
        ('protein', 'Protein'),
        ('fiber', 'Fiber'),
    )

    min_field = forms.ChoiceField(choices=min_choices, required=True)
    budget = forms.IntegerField()
    max_field = forms.ChoiceField(choices=max_choices, required=True)

