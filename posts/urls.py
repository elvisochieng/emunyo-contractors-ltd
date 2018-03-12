from django.urls import path
from . import views

app_name='posts'

urlpatterns = [
	path('', views.list_view, name='list'),
	path('<slug>/', views.detail_view, name='detail'),
]