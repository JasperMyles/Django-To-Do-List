from django.urls import path
from .views import todolist_home, homepage, todo_create, todo_update, todo_delete
app_name = 'todo'

urlpatterns = [
    path('', homepage, name='todo_home'),
    path('todo_list/', todolist_home, name='todo_list'),
    path('todo_create/', todo_create, name='todo_create'),
    path('todo_update/<str:pk>', todo_update, name='todo_update'),
    path('todo_delete/<str:id>',todo_delete, name='todo_delete')
]
