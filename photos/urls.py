from django.urls import path
from . import views

app_name='photos'

urlpatterns = [
	path('', views.button_list, name='button_list'),
	path('cityparents/', views.city_listview, name='city_list'),
	path('manyangwa/', views.manyangwa_listview, name='manyangwa_list'),
	path('makyindye/', views.makyindye_listview, name='makyindye_list'),
]