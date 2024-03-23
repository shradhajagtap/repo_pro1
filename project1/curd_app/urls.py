from django.urls import path
from .views import teacher_view, show_info, update_view, delete_view

urlpatterns = [
    path("", teacher_view, name="teacher_url"),
    path("show/", show_info, name="show_url"),
    path("update/<int:pk>", update_view, name="update_url"),
    path("delete/<int:pk>", delete_view, name="delete_url")
]
