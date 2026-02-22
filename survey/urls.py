from django.urls import path
from . import views
from .views import SurveySubmitAPIView

urlpatterns = [
    path('', views.landing, name='landing'),
    # path('success/', views.success, name='success'),
    path('api/survey/submit/', SurveySubmitAPIView.as_view(), name='api-survey-submit'),
]