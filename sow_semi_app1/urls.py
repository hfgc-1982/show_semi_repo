from django.urls import path, include
from. import views

urlpatterns = [

    path("shows", views.index),
    path("shows/new", views.create_show),
    path("shows/<int:id>", views.show_all, name="all"),
    path("shows/<int:id>/edit", views.show_edit, name="edit"),
    path("shows/<int:id>/destroy", views.show_des, name="destroy"),
]



