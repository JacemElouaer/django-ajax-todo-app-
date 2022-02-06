from django.urls import path
from .views import *
urlpatterns = [
    path('', apiOverview, name="overview"),
    path('tasks_list/', taskList, name="tasks"),
    path('tasks_detail/<int:id>', taskDetail, name="Detail"),
    path('tasks_create/', taskCreate, name="Create"),
    path('tasks_update/<int:id>', taskUpdate, name="Update"),
    path('tasks_delete/<int:id>', taskDelete, name="Delete"),

]

