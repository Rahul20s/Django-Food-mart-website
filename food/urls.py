from django.urls import path
from food import views 

app_name = 'food'

urlpatterns = [

    #http://127.0.0.1:8000/food/home
    path('home/', views.HomeFunctionView, name='home'),
    #path('home/<str:user_types>', views.HomeClassView.as_view(), name='home'),

    #http://127.0.0.1:8000/food/detail/1/
    path('detail/<int:item_id>/', views.DetailFunctionView, name='detail'),
    #path('detail/<int:pk>/', views.DetailClassView.as_view(), name='detail'),

    #http://127.0.0.1:8000/food/add/
    #path('add/',views.CreateFoodItemFunctionView,name='add'),
    path('add/',views.CreateFoodItemClassView.as_view(),name='add'), 

    #http://127.0.0.1:8000/food/update/1/
    path('update/<int:item_id>/', views.UpdateFoodItemFunctionView, name='update'),

    #http://127.0.0.1:8000/food/delete/1
    path('delete/<int:item_id>/', views.DeleteFoodItemFunctionView, name='delete'),
]

