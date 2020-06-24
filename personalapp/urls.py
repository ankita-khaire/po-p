from django.urls import path
from .views import GenericAPIView,NoteAPIView,NoteDetails
from .views import login
# from .views import sample_api


urlpatterns = [
    path('note/', NoteAPIView.as_view()),
    path('detail/<int:id>/', NoteDetails.as_view()),
    path('generic/note/<int:id>/', GenericAPIView.as_view()),
    path('api/login', login),
    # path('api/sampleapi', sample_api)
]