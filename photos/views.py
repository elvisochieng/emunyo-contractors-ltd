from django.shortcuts import render
from .models import Photo

#def list_view(request):
#	queryset = Photo.objects.all()
#	context = {'photos' : queryset}
#	return render(request, 'photos.html', context)

def button_list(request):
	queryset = Photo.objects.all()
	context = {'triggers' : queryset}
	return render(request,'photo_trigger.html', context)

def city_listview(request):
	queryset = Photo.objects.all()
	context = {'photos' : queryset}
	return render(request,'city_photo.html', context)

def manyangwa_listview(request):
	queryset = Photo.objects.all()
	context = {'photos' : queryset}
	return render(request,'manyangwa_photo.html', context)

def makyindye_listview(request):
	queryset = Photo.objects.all()
	context = {'photos' : queryset}
	return render(request,'makyindye_photo.html', context)
