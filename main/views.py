from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.db import models
from .forms import FoodItemForm
from .forms import MinMaxForm
from django_tables2 import SingleTableView
from .tables import FoodItemTable
from .algorithms import minmax_algo

from .models import FoodItem


def menu(request):
    return render(request, 'main/menu.html')


def list(request):
    lowest_price_list = FoodItem.objects.order_by('price')[:5]
    context = {'lowest_price_list': lowest_price_list}
    return render(request, "main/list.html", context)


def details(request, fooditem_id):
    # fooditem = get_object_or_404(FoodItem, pk=fooditem_id)
    # return render(request, "main/details.html", context={"fooditem": fooditem})

    fooditem = get_object_or_404(FoodItem, pk=fooditem_id)
    all_fields = FoodItem._meta.get_fields()

    # Exclude "id", "brand", "name" fields (i.e. elements "0,1,2") since they're part of the /details title
    fields = list(all_fields)[3:]
    list_items = list()
    for field in fields:
        # Keep field_name separate from field.name
        # e.g. "brand" is a field of FootItem (via field.name), but "Brand" is not one (via field_name)
        field_name = field.name.capitalize()
        # Re-retrieve string name of each field
        field_value = getattr(fooditem, field.name)
        # if field_value != -1:  This might not be neccessary anymore
        list_items.append(f"{field_name}: {field_value}")
    return render(request, "main/details.html",
                  context={"fooditem": fooditem, "fields": fields, "list_items": list_items})


def results(request, fooditem_id):
    response = "You're looking at the results for food item #%s."
    return HttpResponse(response % fooditem_id)


def enter(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance_id = instance.id
            # return HttpResponseRedirect("main/")
            return details(request, instance_id)
    else:
        form = FoodItemForm()
    return render(request, 'main/enter.html', {'form': form})


def table(request):
    table_fooditems = FoodItem.objects.all()
    return render(request, 'main/table.html', locals())


class FoodItemListView(SingleTableView):
    model = FoodItem
    table_class = FoodItemTable
    template_name = 'main/listview.html'


def minmax_page(request):
    context = FoodItem.objects.all()

    if request.method == 'POST':
        form = MinMaxForm(request.POST)
        if form.is_valid():
            min_option = form.cleaned_data['min_field']
            min_cap = form.cleaned_data['budget']
            max_option = form.cleaned_data['max_field']

            # Maximizes "max_option" and minimizes "min_option"
            # while allowing a capacity/budget "min_cap" that cannot be exceeded for min_option
            algo_result_dict, algo_result_val = minmax_algo(min_option, min_cap, max_option, context)

            return render(request, 'main/result.html',
                          {'min_field': min_option, 'min_cap': min_cap, 'max_field': max_option,
                           'algo_dict': algo_result_dict, 'algo_val': algo_result_val})
    else:
        form = MinMaxForm()
    return render(request, 'main/dropdown_form.html', {'form': form})


def myminmax(request):
    myminmax_list = FoodItem.objects.order_by('price')[:5]
    context = {'myminmax_list': myminmax_list}
    return render(request, "main/myminmax.html", context)
