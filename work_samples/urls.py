from django.urls import path
from . import views as worksample_views
urlpatterns = [
    path('list', worksample_views.WorkSampleListApiView.as_view(),
         name='list work samples'),
    path('<str:slug>', worksample_views.WorkSampleRetrieveView.as_view(),
         name='get work sample details')

]
