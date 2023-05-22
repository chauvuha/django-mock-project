from django.urls import path

# just import from the views so we can render that 
from . import views 

# get the function getRoutes from views
# Everything with <str:p> is the p parameter for the functions in views.py
urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('/notes/', views.getNotes, name="notes"),
    path('/note/<str:p>/', views.getNote, name="note"),
    path('/note/create', views.createNote),
    path('/note/<str:p>/update', views.updateNote),
    path('/note/<str:p>/delete', views.deleteNote)
]