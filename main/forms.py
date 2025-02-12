from django import forms
from django.forms import ModelForm
from .models import FoodItem


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