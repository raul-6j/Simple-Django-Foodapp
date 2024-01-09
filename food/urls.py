from . import views
from django.urls import path


app_name = 'food'

urlpatterns = [
    #food
    # path('', views.index, name='index'),
    #food_classbased
    path('', views.indexClassView.as_view(),name='index'),

    #detail
    # path('<int:item_id>/',views.detail, name='detail'),
    #detail_classbased
    path('<int:pk>/',views.foodDetail.as_view(), name='detail'),

    #add items
    # path('add/',views.create_item,name='create_item'),
    #class_based_additem
    path('add/',views.createItem.as_view(),name='create_item'),


    #update_item
    path('edit/<int:item_id>/',views.update_item,name='update_item'),
    #delete_item
    path('delete/<int:item_id>/',views.delete_item,name='delete_item'),


    # path('item/', views.item, name='item'),


]
