from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'ads'

urlpatterns =[
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
