from django.urls import path
from task.views import createTask, editTask, deleteTask

urlpatterns = [
    path("create/", createTask, name="create_task"),
    path("edit/<int:t_id>", editTask, name="edit_task"),
    path("delete/<int:t_id>", deleteTask, name="delete_task"),
]
