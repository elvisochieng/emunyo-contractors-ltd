from django.db import models

class Photo(models.Model):
	title = models.CharField(max_length=100)
	category = models.CharField(max_length=100, default='_photo')
	width = models.IntegerField(default=0)
	height = models.IntegerField(default=0)
	image = models.ImageField(null=False, blank=False, width_field='width', height_field='height')
	date = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return self.title

	class Meta:
		ordering : ['-date']
