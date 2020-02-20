from django.urls import path
from .views import SignUpView

urlpatterns = [
    #Path registration
    path('signup/', SignUpView.as_view(), name='signup'),
]