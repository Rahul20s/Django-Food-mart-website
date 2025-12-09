from django.shortcuts import render, redirect
from django.http import HttpResponse
from food.models import FoodItemsModel, LogHistoryModel
from food.forms import FoodItemsForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy



# Create your views here.
# ---------------------------------------------------------------------------------------------

# function based home view
# ---------------------------------------------------------------------------------------------
def HomeFunctionView(request):
    if request.user.is_authenticated and request.user.profilemodel.user_types == "ADMIN":
        item_list = FoodItemsModel.objects.all()

    elif request.user.is_authenticated and request.user.profilemodel.user_types == "CUSTOMER":
                item_list = FoodItemsModel.objects.all()

    elif request.user.is_authenticated and request.user.profilemodel.user_types == "RESTAURANT":
        item_list = FoodItemsModel.objects.filter(restaurant_owner=request.user.id)

    else:
        item_list = FoodItemsModel.objects.all()

    context = {
        "item_list": item_list
    }
   
    return render(request, "food/home.html", context)


#Class based home view
#------------------------------------------------------------------------------------------------
class HomeClassView(ListView):
    model = FoodItemsModel
    context_object_name = "item_list"
    template_name = "food/home.html"



# function based detail view
# ---------------------------------------------------------------------------------------------
def DetailFunctionView(request, item_id):
    item = FoodItemsModel.objects.get(id=item_id)
    object_lh=LogHistoryModel.objects.filter(
         log_prod_code = item.prod_code
    )
   
    context = {
        'item': item,
        'object_lh': object_lh
    }
   
    return render(request, "food/detail.html", context)


#Class based detail view
#----------------------------------------------------------------------------------------------
class DetailClassView(DetailView):
    model = FoodItemsModel
    context_object_name = 'item'
    template_name = "food/detail.html"


# function based create item view
# ---------------------------------------------------------------------------------------------
def CreateFoodItemFunctionView(request):
    form = FoodItemsForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("food:home")
   
    context = {
        'form': form
    }
   
    return render(request, "food/food-items-form.html", context)

#Class based create item view
#--------------------------------------------------------------------------------------------------
class CreateFoodItemClassView(CreateView):
    model = FoodItemsModel
    fields = ['prod_code','restaurant_owner','item_name','item_description','item_price','item_image']
    template_name = "food/food-items-form.html"
    success_url = reverse_lazy("food:home")

    def form_valid(self, form):
        form.instance.admin = self.request.user.username
        
        object_log_history = LogHistoryModel(
             log_prod_code = form.instance.prod_code,               #self.request.POST.get('prod_code')
             log_username = self.request.user.username,
             log_item_name = form.instance.item_name,               #self.request.POST.get('item_name')
             log_operation_type = 'created',
        )
        object_log_history.save()

        return super().form_valid(form)


# function based update item view
# ---------------------------------------------------------------------------------------------
def UpdateFoodItemFunctionView(request, item_id):
    item = FoodItemsModel.objects.get(id=item_id)
    form = FoodItemsForm(request.POST or None, instance=item)
   
    context = {
        'form': form
    }
   
    if form.is_valid():
        form.save()
        
        object_log_history = LogHistoryModel(
             log_prod_code = form.instance.prod_code,               #self.request.POST.get('prod_code')
             log_username = request.user.username,
             log_item_name = form.instance.item_name,               #self.request.POST.get('item_name')
             log_operation_type = 'updated',
        )
        object_log_history.save()

        return redirect('food:detail', item_id=item_id)
   
    return render(request, "food/food-items-form.html", context)


# function based delete item view
# ---------------------------------------------------------------------------------------------
def DeleteFoodItemFunctionView(request, item_id):
    item = FoodItemsModel.objects.get(id=item_id)
   
    context = {
        'item': item
    }
   
    if request.method == 'POST':
        object_log_history = LogHistoryModel(
             log_prod_code = item.prod_code,               #self.request.POST.get('prod_code')
             log_username = request.user.username,
             log_item_name = item.item_name,               #self.request.POST.get('item_name')
             log_operation_type = 'deleted',
        )
        object_log_history.save()

        
        item.delete()
        return redirect('food:home')
   
    return render(request, "food/item-delete.html", context)