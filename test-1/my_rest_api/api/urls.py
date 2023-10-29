from django.urls import path
from .views import MyRestAPI

urlpatterns = [
    # path('', MyRestAPI.as_view()),
    # path('create/',MyRestAPI.as_view()),
    # path('update/<int:id>/',MyRestAPI.as_view()),
    # path('delete/<int:id>/',MyRestAPI.as_view()),

    path('getAll/', MyRestAPI.as_view(), name='get_items_all'),
    path('getByID/<int:id>/', MyRestAPI.as_view(), name='get_item_by_id'),
    path('create/', MyRestAPI.as_view(), name='create_item'),
    path('update/<int:id>/', MyRestAPI.as_view(), name='update_item'),
    path('delete/<int:id>/', MyRestAPI.as_view(), name='delete_item'),

]