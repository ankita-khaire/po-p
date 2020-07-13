from django.urls import path
from .views import NoteAPIView,NoteDetails, Registration_view
from .views import login



urlpatterns = [
    path('note', NoteAPIView.as_view()),
    path('note/<int:id>', NoteDetails.as_view()),
    path('login', login),
    path('register', Registration_view,name="register"),
]