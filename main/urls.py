from django.urls import path
from .views import HomeView,UploatView,AnalysisView,Save

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('upload/',UploatView.as_view(),name='upload'),
    path('analysis/',AnalysisView.as_view(),name='analyze'),
    # path('download/',DownloadReportView.as_view(),name='download'),
    path('save/',Save.as_view(),name='save'),
]
