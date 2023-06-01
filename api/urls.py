from django.urls import path

# just import from the views so we can render that 
from . import views 

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

# get the function getRoutes from views
# Everything with <str:p> is the p parameter for the functions in views.py
urlpatterns = [
    path('', views.RoutesView.as_view(), name="routes"),
    path('notes/', views.NotesListView.as_view(), name="notes"),
    path('note/create/', views.CreateNoteView.as_view()),
    path('note/<str:p>/', views.NoteView.as_view(), name="note"),
    path('note/<str:p>/update/', views.UpdateNoteView.as_view()),
    path('note/<str:p>/delete/', views.DeleteNoteView.as_view()),
    # path('register/', views.register_view, name='register'),
]