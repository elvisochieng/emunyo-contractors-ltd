from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	width = models.IntegerField(default=0)
	height = models.IntegerField(default=0)
	image = models.ImageField(null=True, blank=True, width_field='width', height_field='height')
	slug = models.SlugField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def snippet(self):
		return self.body[:100]+"..."

	class Meta:
		ordering = ['-date']
